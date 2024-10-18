import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from App import logic as l
from tabulate import tabulate
import time as time
from DataStructures.List import array_list as lt


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

    control = l.load_data(control, "Data/Challenge-2/movies-small.csv")
    f = 0
    g=0
    
    for i in range(control["capacity"]):
        if control["table"]["elements"][i]["key"] is not None and f < 5:
            print_data(control, control["table"]["elements"][i]["key"])
            f += 1
        if f >= 5:
            break
    for i in range(control["capacity"] - 1, -1, -1):  # Iterar hacia atrás
        if control["table"]["elements"][i]["key"] is not None and g < 5:
            print_data(control, control["table"]["elements"][i]["key"])
            g += 1
        if g >= 5:
            break
    print(f'Se cargaron {control["size"]} películas en el catálogo.')
    return control


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    # Realizar la función para imprimir un elemento
    requirements = ["id", "title", "original_language", "release_date", "revenue", "runtime" ,"status", "vote_average" ,"vote_count", "budget", "genres", "production_companies", "earnings"]
    movie_data = l.get_data(control, id, requirements)
    if movie_data:
        print(f"Datos de la película con ID {id}:")
        print(requirements)
        print(tabulate([movie_data.values()], tablefmt="github"))
    else:
        print("No se encontró una película con ese ID.")


def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    #  Imprimir el resultado del requerimiento 1
    name = input("Ingrese el nombre de la película: ")
    language = input("Ingrese el idioma original: ")
    tiempo_inicial = time.time()
    result, size, requirements = l.req_1(control, name, language)
    tiempo_final = time.time()
    if size == 0:
        print("No se encontraron películas que cumplieran con los criterios")
    else:
        print(f"Se encontró la película '{name}' en el idioma '{language}':")

        print(tabulate([result["elements"]], headers=requirements, tablefmt="github"))
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
    language = input("Ingrese el idioma original: ")
    start_date = input("Ingrese la fecha de inicio: ")
    end_date = input("Ingrese la fecha final: ")    
    tiempo_inicial = time.time()
    size, average_duration, info, requirements = l.req_3(control, language, start_date, end_date)
    tiempo_final = time.time()
    print(f"Se encontraron {size} películas que cumplen los criterios, con una duración promedio de {average_duration} minutos")
    print(requirements)
    print(tabulate(info["elements"], tablefmt="github" ))
    print(f"Tiempo de ejecución: {l.delta_time(tiempo_inicial, tiempo_final)} ms")


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    be = input("Ingrese el estado de la película: ")
    start_date = input("Ingrese la fecha de inicio: ")
    end_date = input("Ingrese la fecha final: ")
    tiempo_inicial = time.time()
    size, average_duration, info, requirements = l.req_4(control, be, start_date, end_date)
    tiempo_final = time.time()
    print(f"Se encontraron {size} películas que cumplen los criterios, con una duración promedio de {average_duration} minutos")
    print(requirements)
    print(tabulate(info["elements"], tablefmt="github" ))
    print(f"Tiempo de ejecución: {l.delta_time(tiempo_inicial, tiempo_final)} ms")



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
    language = input("Ingrese el idioma deseado: ")
    start_year = int(input("Ingrese el año de inicio: "))
    end_year = int(input("Ingrese el año final: "))
    tiempo_inicial = time.time()
    result = l.req_6(control, language, start_year, end_year)
    tiempo_final = time.time()
    headers = ["year", "total movies", "total duration", "total earnings", "best movie (rating)", "worst movie (rating)"]
    ans = []
    if result != {}:
        for year in range(start_year, end_year+1):
            data = [
            year,
            result[year]['total_peliculas'],
            result[year]['total_duracion'],
            result[year]['total_ganancias'],
            f"{result[year]['mejor_pelicula'][0]} ({result[year]['mejor_pelicula'][1]})",
            f"{result[year]['peor_pelicula'][0]} ({result[year]['peor_pelicula'][1]})"
                ]
            ans.append(data)
        print(tabulate(ans, headers , tablefmt="github"))
    else:
        print(f"No se encontraron resultados para el idioma '{language}' entre {start_year} y {end_year}.")
    print(f"Tiempo de ejecución: {l.delta_time(tiempo_inicial, tiempo_final)} ms")



def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    #  Imprimir el resultado del requerimiento 7
    company = input("Ingrese la compañía productora: ")
    start_year = int(input("Ingrese el año de inicio: "))
    end_year = int(input("Ingrese el año final: "))
    tiempo_inicial = time.time()
    result = l.req_7(control, company, start_year, end_year)  # Pasar correctamente los parámetros
    tiempo_final = time.time()
    ans = []
    headers = ["year", "total movies", "total duration", "total earnings", "best movie (rating)", "worst movie (rating)"]
    if result:
        for year in result:
            stats = [
                year,
                result[year]['total_peliculas'],
                result[year]['total_duracion'],
                result[year]['total_ganancias'],
                f"{result[year]['mejor_pelicula'][0]} ({result[year]['mejor_pelicula'][1]})",
                f"{result[year]['peor_pelicula'][0]} ({result[year]['peor_pelicula'][1]})"
                ]
            ans.append(stats)
            lt.merge_sort(ans, sort_criteria_increasingly)
            print(tabulate(ans, headers, tablefmt="github"))
    else:
        print(f"No se encontraron resultados para la compañía '{company}' entre los años {start_year} y {end_year}.")
    print(f"Tiempo de ejecución: {l.delta_time(tiempo_inicial, tiempo_final)} ms")



def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    #  Imprimir el resultado del requerimiento 8
    genero = input("Ingrese el género: ")
    start_year = int(input("Ingrese el año de inicio: "))
    tiempo_inicial = time.time()
    resultado = l.req_8(control, genero, start_year)  # Pasar correctamente los parámetros
    tiempo_final = time.time()
    
    if resultado:
        for year in range(start_year, start_year+1000):
            if year in resultado:
                    print(f"Año: {year}")
                    print(f"Total películas: {resultado[year]['total_peliculas']}")
                    print(f"Duración total: {resultado[year]['total_duracion']} minutos")
                    print(f"Ganancias totales: ${resultado[year]['total_ganancias']}")
                    print(f"Mejor película: {resultado[year]['mejor_pelicula'][0]} con calificación {resultado[year]['mejor_pelicula'][1]}")
                    print(f"Peor película: {resultado[year]['peor_pelicula'][0]} con calificación {resultado[year]['peor_pelicula'][1]}")
                    print("-------------------------------------------------------")
    else:
        print(f"No se encontraron resultados para el género '{genero}' desde el año {start_year}.")
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
if __name__ == "__main__":
    main()