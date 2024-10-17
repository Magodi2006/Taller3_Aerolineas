import time
from DataStructures.Map import map_linear_probing as lp
from DataStructures.List import array_list as lt

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    catalog = { "id" : None,
                "title" : None,
                "original_language" : None,
                "release_date": None,
                "revenue" : None,
                "runtime" : None,
                "status" : None,
                "vote_average" : None,
                "vote_count" : None,
                "budget" : None,
                "genres" : None,
                "production_companies" : None
                }
    
    catalog["id"] = lt.new_list()
    catalog["title"] = lt.new_list()
    catalog["original_language"] = lt.new_list()
    catalog["release_date"] = lt.new_list()
    catalog["revenue"] = lt.new_list()
    catalog["runtime"] = lt.new_list()
    catalog["status"] = lt.new_list()
    catalog["vote_average"] = lt.new_list()
    catalog["vote_count"] = lt.new_list()
    catalog["budget"] = lt.new_list()
    catalog["genres"] = lt.new_list()
    catalog["production_companies"] = lt.new_list()
    #TODO: Llama a las funciónes de creación de las estructuras de datos
    pass


# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    pass

# Funciones de consulta sobre el catálogo

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Consulta en las Llamar la función del modelo para obtener un dato
    pass


def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(catalog):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(catalog):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
