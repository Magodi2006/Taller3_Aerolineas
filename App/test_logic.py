import sys
import os

# Agregar la carpeta superior a la ruta de búsqueda de módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



import pandas as pd
from App import logic

# Cargar el archivo CSV para extraer los parámetros y valores esperados
file_path = 'C:/Users/magod/Downloads/Challenge-2/Reto2-G03/Data/movies-small.csv'  # Cambia esto a la ruta correcta de tu archivo CSV
df = pd.read_csv(file_path)

# Definición de parámetros y valores esperados
# Cambia 'columna_con_parametros' y los nombres de las columnas según tu archivo CSV
parametros = df['Title'].tolist()  # Asumiendo que deseas usar los títulos de las películas como parámetros
valor_esperado_1 = df['Rating'].iloc[0]  # Ajusta según la columna correcta para el valor esperado 1
valor_esperado_6 = df['Revenue'].iloc[0]  # Ajusta para el valor esperado 6
valor_esperado_7 = df['Duration'].iloc[0]  # Ajusta para el valor esperado 7
valor_esperado_8 = df['Genre'].iloc[0]  # Ajusta para el valor esperado 8

def test_requerimiento_1():
    resultado = logic.funcion_requerimiento_1(parametros)
    assert resultado == valor_esperado_1

def test_requerimiento_6():
    resultado = logic.funcion_requerimiento_6(parametros)
    assert resultado == valor_esperado_6

def test_requerimiento_7():
    resultado = logic.funcion_requerimiento_7(parametros)
    assert resultado == valor_esperado_7

def test_requerimiento_8():
    resultado = logic.funcion_requerimiento_8(parametros)
    assert resultado == valor_esperado_8
