import sys
import App.logic as l
from tabulate import tabulate
import time as time



def new_logic():
    """
        Se crea una instancia del controlador
    """
    # Llamar la función de la lógica donde se crean las estructuras de datos
    control = l.new_logic()
    return control

def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8 (Bono)")
    print("0- Salir")

def load_data(control):
    """
    Carga los datos
    """
    # Realizar la carga de datos
    filename = input("Ingrese el nombre del archivo CSV a cargar (con la ruta si es necesario): ")
    control = l.load_data(control, filename)
    n_data = control["id"]["size"]
    print(f"Se cargaron {n_data} películas en el catálogo.")
    return control


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    # Realizar la función para imprimir un elemento
    movie_data = l.get_data(control, id)
    if movie_data:
        print(f"Datos de la película con ID {id}:")
        print(tabulate([movie_data.values()], movie_data.keys(), tablefmt="github"))
    else:
        print("No se encontró una película con ese ID.")


def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    #  Imprimir el resultado del requerimiento 1
    nombre_pelicula = input("Ingrese el nombre de la película: ")
    idioma = input("Ingrese el idioma original: ")
    tiempo_inicial = time.time()
    resultado = l.req_1(control)
    tiempo_final = time.time()
    if resultado == "Película no encontrada":
        print(resultado)
    else:
        print(f"Se encontró la película '{nombre_pelicula}' en el idioma '{idioma}':")
        print(tabulate(resultado, headers="keys", tablefmt="github"))
    print(f"Tiempo de ejecución: {l.delta_time(tiempo_inicial, tiempo_final)} ms")



def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    #  Imprimir el resultado del requerimiento 6
    idioma = input("Ingrese el idioma deseado: ")
    anio_inicio = int(input("Ingrese el año de inicio: "))
    anio_fin = int(input("Ingrese el año final: "))
    tiempo_inicial = time.time()
    resultado = l.req_6(control)
    tiempo_final = time.time()
    if resultado:
        for anio, datos in resultado.items():
            print(f"Año: {anio}")
            for key, value in datos.items():
                print(f"{key}: {value}")
            print("-------------------------------------------------------")
    else:
        print(f"No se encontraron resultados para el idioma '{idioma}' entre {anio_inicio} y {anio_fin}.")
    print(f"Tiempo de ejecución: {l.delta_time(tiempo_inicial, tiempo_final)} ms")



def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    #  Imprimir el resultado del requerimiento 7
    compania = input("Ingrese la compañía productora: ")
    anio_inicio = int(input("Ingrese el año de inicio: "))
    anio_fin = int(input("Ingrese el año final: "))
    tiempo_inicial = time.time()
    resultado = l.req_7(control, compania, anio_inicio, anio_fin)  # Pasar correctamente los parámetros
    tiempo_final = time.time()
    
    if resultado:
        for anio, datos in resultado.items():
            print(f"Año: {anio}")
            print(f"Total películas: {datos['total_peliculas']}")
            print(f"Duración total: {datos['total_duracion']} minutos")
            print(f"Ganancias totales: ${datos['total_ganancias']}")
            print(f"Mejor película: {datos['mejor_pelicula'][0]} con calificación {datos['mejor_pelicula'][1]}")
            print(f"Peor película: {datos['peor_pelicula'][0]} con calificación {datos['peor_pelicula'][1]}")
            print("-------------------------------------------------------")
    else:
        print(f"No se encontraron resultados para la compañía '{compania}' entre los años {anio_inicio} y {anio_fin}.")
    print(f"Tiempo de ejecución: {l.delta_time(tiempo_inicial, tiempo_final)} ms")



def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    #  Imprimir el resultado del requerimiento 8
    genero = input("Ingrese el género: ")
    anio_inicio = int(input("Ingrese el año de inicio: "))
    tiempo_inicial = time.time()
    resultado = l.req_8(control, genero, anio_inicio)  # Pasar correctamente los parámetros
    tiempo_final = time.time()
    
    if resultado:
        for anio, datos in resultado.items():
            print(f"Año: {anio}")
            print(f"Total películas: {datos['total_peliculas']}")
            print(f"Duración total: {datos['total_duracion']} minutos")
            print(f"Ganancias totales: ${datos['total_ganancias']}")
            print(f"Mejor película: {datos['mejor_pelicula'][0]} con calificación {datos['mejor_pelicula'][1]}")
            print(f"Peor película: {datos['peor_pelicula'][0]} con calificación {datos['peor_pelicula'][1]}")
            print("-------------------------------------------------------")
    else:
        print(f"No se encontraron resultados para el género '{genero}' desde el año {anio_inicio}.")
    print(f"Tiempo de ejecución: {l.delta_time(tiempo_inicial, tiempo_final)} ms")


# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
