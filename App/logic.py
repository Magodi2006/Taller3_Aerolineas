import time
import csv
import json
import datetime
from DataStructures.Map import map_linear_probing as lp
from DataStructures.List import array_list as lt

def sort_criteria_increasingly(element1, element2):
    is_sorted = False
    if element1 <= element2:
        is_sorted = True
    return is_sorted

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    catalog = lp.new_map(15000, 0.7)
    
    return catalog


# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    movies = csv.DictReader(open(filename, encoding='utf-8'))
    for movie in movies:
        key = movie["id"]
        value = { "id" : None,
                "title" : None,
                "original_language" : None,
                "release_date": None,
                "revenue" : None,
                "runtime" : None,
                "status" : None,
                "vote_average" : None,
                "vote_count" : None,
                "budget" : None,
                "genres" : lt.new_list(),
                "production_companies" : lt.new_list(),
                "earnings" : None
                }
        for resource in value:
            if resource != "genres"and resource != "production_companies" and resource != "earnings":
                if movie[resource] is not None or movie["value"] != "":
                    value[resource] = movie[resource]
                else:
                    value[resource] = "Unknown"
            if resource == "genres":
                for genre in json.loads(movie["genres"]):
                    lt.add_last(value["genres"], [genre["id"], genre["name"]])
            if resource == "production_companies":
                for companie in json.loads(movie["production_companies"]):
                    lt.add_last(value["production_companies"], [companie["id"], companie["name"]])
            if resource == "earnings":
                if movie["budget"] not in [None, ""] and movie["revenue"] not in [None, ""]:
                    value["earnings"] = float(movie["revenue"]) - float(movie["budget"])
                else:
                    value["earnings"] = "Undefined"
        lp.put(catalog, key, value)
    return catalog

# Funciones de consulta sobre el catálogo

def get_data(catalog, id, requirements):
    """
    Retorna un dato por su ID.
    """
    #TODO: Consulta en las Llamar la función del modelo para obtener un dato
    present = lp.contains(catalog, id)
    ans = lt.new_list()
    if present:
        temp = lp.get(catalog, id)
        for requirement in requirements:
            lt.add_last(ans, temp[requirement])
        return ans
    return ans

def req_1(catalog, name, language):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    requirements = ["runtime", "release_date", "revenue", "budget", "earnings", "vote_average", "original_language"]
    filtro = lt.new_list()
    ans = None
    for movie in catalog["table"]["elements"]:
        if movie["value"] != None:
            if movie["value"]["original_language"] == language and movie["value"]["title"].lower() == name.lower():
                lt.add_last(filtro, movie["key"])
    for key in filtro["elements"]:
        ans = get_data(catalog, key, requirements)
    if ans == None:
        ans = []
    return ans, filtro["size"], requirements
    

def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog, language, start_date, end_date):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    requirements = ["release_date", "title", "budget", "revenue", "earnings", "runtime", "vote_average", "status"]
    start_year, star_month, start_day = start_date.split("-")
    start_date = datetime.date(int(start_year), int(star_month), int(start_day))
    end_year, end_month, end_day = end_date.split("-")
    end_date = datetime.date(int(end_year), int(end_month), int(end_day))
    id_filtered_movies = lt.new_list()
    total_duration = 0
    ans = lt.new_list()
    for couple in catalog["table"]["elements"]:
        if couple["key"] != None:
            year, month, day = couple["value"]["release_date"].split("-")
            date = datetime.date(int(year), int(month), int(day))
            if couple["value"]["original_language"]==language and (start_date<=date<= end_date):
                lt.add_last(id_filtered_movies, couple["key"])
                runtime = float(couple["value"]["runtime"]) if couple["value"]["runtime"] not in [None, "", "Unknown"] else 0
                total_duration += runtime


    if id_filtered_movies["size"]>20:
        size = id_filtered_movies["size"]
        search = [0,1,2,3,4,size-5,size-4,size-3,size-2,size-1]
        for i in search:
            lt.add_last(ans, get_data(catalog, id_filtered_movies["elements"][i], requirements))
    else:
        for key in id_filtered_movies["elements"]:
            lt.add_last(ans, get_data(catalog, key, requirements))

    if id_filtered_movies["size"] != 0:
        average_duration = total_duration/id_filtered_movies["size"]
    else:
        average_duration = 0
    return id_filtered_movies["size"], average_duration, ans, requirements


def req_4(catalog, be, start_date, end_date):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    requirements = ["release_date", "title", "budget", "revenue", "earnings", "runtime", "vote_average", "original_language"]
    start_year, star_month, start_day = start_date.split("-")
    start_date = datetime.date(int(start_year), int(star_month), int(start_day))
    end_year, end_month, end_day = end_date.split("-")
    end_date = datetime.date(int(end_year), int(end_month), int(end_day))
    id_filtered_movies = lt.new_list()
    total_duration = 0
    ans = lt.new_list()
    for couple in catalog["table"]["elements"]:
        if couple["key"] != None:
            year, month, day = couple["value"]["release_date"].split("-")
            date = datetime.date(int(year), int(month), int(day))
            if couple["value"]["status"].lower() == be.lower() and (start_date<=date<= end_date):
                lt.add_last(id_filtered_movies, couple["key"])
                total_duration += float(couple["value"]["runtime"]) if couple["value"]["runtime"] not in ["", None, "Unknown"] else 0
    
    if id_filtered_movies["size"]>20:
        size = id_filtered_movies["size"]
        search = [0,1,2,3,4,size-5,size-4,size-3,size-2,size-1]
        for i in search:
            lt.add_last(ans, get_data(catalog, id_filtered_movies["elements"][i], requirements))
    else:
        for key in id_filtered_movies["elements"]:
            lt.add_last(ans, get_data(catalog, key, requirements))
            
    if id_filtered_movies["size"] != 0:
        average_duration = total_duration/id_filtered_movies["size"]
    else:
        average_duration = 0
    return id_filtered_movies["size"], average_duration, ans, requirements

def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog, language, start_year, end_year):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    result = {}
    for couple in catalog["table"]["elements"]:
        if couple["key"] != None:
            original_language = couple["value"]["original_language"]
            date = couple["value"]["release_date"]
            
            if date != "undefined":
                year = int(date.split('-')[0])
                if original_language == language and start_year <= year <= end_year:
                    if year not in result:
                        result[year] = {
                            'total_peliculas': 0,
                            'total_duracion': 0,
                            'total_ganancias': 0,
                            'mejor_pelicula': [None, float(couple["value"]["vote_average"])-1],
                            'peor_pelicula': [None, float(couple["value"]["vote_average"])+1]
                        }
                    duration = couple["value"]["runtime"] if couple["value"]["runtime"] not in ["", None, "Unknown"] else 0
                    earnings = couple["value"]["earnings"] if couple["value"]["earnings"] not in ["", None, "Unknown"] else 0
                    
                    result[year]['total_peliculas'] += 1
                    result[year]['total_duracion'] += float(duration)
                    result[year]['total_ganancias'] += float(earnings)
                    
                    calificacion = float(couple["value"]["vote_average"]) if couple["value"]["vote_average"] not in ["", None, "Unknown"] else 0
                    if calificacion > result[year]['mejor_pelicula'][1]:
                        result[year]['mejor_pelicula'][1] = calificacion 
                        result[year]["mejor_pelicula"][0] = couple["value"]["title"]
                    if calificacion < result[year]['peor_pelicula'][1]:
                        result[year]['peor_pelicula'][1] = calificacion
                        result[year]["peor_pelicula"][0] = couple["value"]["title"]
    return result


def req_7(catalog, name_companie, start_year, end_year):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    result = {}
    for couple in catalog['table']["elements"]:
        if couple["key"] != None:
            year = int(couple["value"]['release_date'].split('-')[0])
            for company in couple["value"]['production_companies']["elements"]:
                if name_companie.lower() == company[1].lower() and start_year <= year <= end_year:
                    if year not in result:
                        result[year] = {
                            'total_peliculas': 0,
                            'total_duracion': 0,
                            'total_ganancias': 0,
                            'mejor_pelicula': ('', -float('inf')),
                            'peor_pelicula': ('', float('inf'))
                        }
                    vote_average = float(couple["value"]['vote_average']) if couple["value"]['vote_average'] not in [None, "", "Unknown"] else 0
                    runtime = float(couple["value"]['runtime']) if couple["value"]['runtime'] not in [None, "", "Unknown"] else 0
                    earnings = float(couple["value"]["earnings"]) if couple["value"]["earnings"] not in [None, "", "Undefined"] else 0
                    result[year]['total_peliculas'] += 1
                    result[year]['total_duracion'] += runtime
                    result[year]['total_ganancias'] += earnings
                    if vote_average > result[year]['mejor_pelicula'][1]:
                        result[year]['mejor_pelicula'] = (couple["value"]['title'], vote_average)
                    if vote_average < result[year]['peor_pelicula'][1]:
                        result[year]['peor_pelicula'] = (couple["value"]['title'], vote_average)

    return result


def req_8(catalog, name_genre, start_year):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    result = {}
    for couple in catalog["table"]["elements"]:
        if couple["key"] != None:
            year = int(couple["value"]['release_date'].split('-')[0])
            for genre in couple["value"]["genres"]["elements"]:
                if name_genre.lower() == genre[1].lower() and year >= start_year and couple["value"]["status"]=="Released":
                    if year not in result:
                        result[year] = {
                            'total_peliculas': 0,
                            'total_duracion': 0,
                            'total_ganancias': 0,
                            'mejor_pelicula': ('', -float('inf')),
                            'peor_pelicula': ('', float('inf'))
                        }
                    duration = float(couple["value"]['runtime']) if couple["value"]['runtime'] not in [None, "", "Unknown"] else 0
                    earnings = float(couple["value"]["earnings"]) if couple["value"]["earnings"] not in [None, "", "Undefined"] else 0
                    rating = float(couple["value"]['vote_average']) if couple["value"]['vote_average'] not in [None, "", "Unknown"] else 0
                    result[year]['total_peliculas'] += 1
                    result[year]['total_duracion'] += duration
                    result[year]['total_ganancias'] += earnings
                    if rating > float(result[year]['mejor_pelicula'][1]):
                        result[year]['mejor_pelicula'] = (couple["value"]['title'], couple["value"] ['vote_average'])
                    if rating < float(result[year]['peor_pelicula'][1]):
                        result[year]['peor_pelicula'] = (couple["value"]['title'], couple["value"]['vote_average'])

    return result


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
