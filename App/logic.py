import time
import csv
import json
import datetime
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
    return catalog


# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    movies = csv.DictReader(open(filename, encoding='utf-8'))
    for movie in movies:
        
        genres_list = json.loads(movie["genres"])
        genres_associated = [{"id": genre["id"], "name": genre["name"]} if genre else {"id": 0, "name": "bono de 0.5"} for genre in genres_list]
        lt.add_last(catalog["genres"], genres_associated)

        
        company_list = json.loads(movie["production_companies"])
        company_associated = [{"id": company["id"], "name": company["name"]} if company else {"id": 0, "name": "bono de 0.5"} for company in company_list]
        lt.add_last(catalog["production_companies"], company_associated)
        
        
        lt.add_last(catalog["id"], movie.get("id", "undefined"))
        lt.add_last(catalog["title"], movie.get("title", "undefined"))
        lt.add_last(catalog["original_language"], movie.get("original_language", "undefined"))
        lt.add_last(catalog["release_date"], movie.get("release_date", "undefined"))
        lt.add_last(catalog["revenue"], movie.get("revenue", "undefined"))
        lt.add_last(catalog["runtime"], movie.get("runtime", "undefined"))
        lt.add_last(catalog["status"], movie.get("status", "undefined"))
        lt.add_last(catalog["vote_average"], movie.get("vote_average", "undefined"))
        lt.add_last(catalog["vote_count"], movie.get("vote_count", "undefined"))
        lt.add_last(catalog["budget"], movie.get("budget", "undefined"))

    return catalog

# Funciones de consulta sobre el catálogo

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Consulta en las Llamar la función del modelo para obtener un dato
    pos = lt.is_present(catalog["id"], id)
    if pos != -1:
        movie_data = {
            "id": lt.get_element(catalog["id"], pos),
            "title": lt.get_element(catalog["title"], pos),
            "original_language": lt.get_element(catalog["original_language"], pos),
            "release_date": lt.get_element(catalog["release_date"], pos),
            "revenue": lt.get_element(catalog["revenue"], pos),
            "runtime": lt.get_element(catalog["runtime"], pos),
            "status": lt.get_element(catalog["status"], pos),
            "vote_average": lt.get_element(catalog["vote_average"], pos),
            "vote_count": lt.get_element(catalog["vote_count"], pos),
            "budget": lt.get_element(catalog["budget"], pos),
            "genres": lt.get_element(catalog["genres"], pos),
            "production_companies": lt.get_element(catalog["production_companies"], pos)
        }
        return movie_data
    else:
        return None


def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    resultado = []
    size = lt.size(catalog['title'])
    
    for i in range(size):
        titulo = lt.get_element(catalog['title'], i)
        lang = lt.get_element(catalog['original_language'], i)
        
        if titulo == nombre_pelicula and lang == idioma:
            pelicula = {
                'titulo_original': titulo,
                'duracion': lt.get_element(catalog['runtime'], i),
                'fecha_publicacion': lt.get_element(catalog['release_date'], i),
                'presupuesto': lt.get_element(catalog['budget'], i),
                'ingresos': lt.get_element(catalog['revenue'], i),
                'ganancias': float(lt.get_element(catalog['revenue'], i)) - float(lt.get_element(catalog['budget'], i)),
                'calificacion': lt.get_element(catalog['vote_average'], i),
                'idioma_original': lang
            }
            resultado.append(pelicula)
    
    return resultado if resultado else "Película no encontrada"

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
    resultado = {}
    size = lt.size(catalog['title'])
    
    for i in range(size):
        lang = lt.get_element(catalog['original_language'], i)
        fecha = lt.get_element(catalog['release_date'], i)
        
        if fecha != "undefined":
            anio = int(fecha.split('-')[0])
            if lang == idioma and anio_inicio <= anio <= anio_fin:
                if anio not in resultado:
                    resultado[anio] = {
                        'total_peliculas': 0,
                        'total_duracion': 0,
                        'total_ganancias': 0,
                        'mejor_pelicula': ('', -float('inf')),
                        'peor_pelicula': ('', float('inf'))
                    }
                duracion = lt.get_element(catalog['runtime'], i)
                ganancias = float(lt.get_element(catalog['revenue'], i)) - float(lt.get_element(catalog['budget'], i))
                
                resultado[anio]['total_peliculas'] += 1
                resultado[anio]['total_duracion'] += float(duracion)
                resultado[anio]['total_ganancias'] += ganancias
                
                calificacion = float(lt.get_element(catalog['vote_average'], i))
                if calificacion > resultado[anio]['mejor_pelicula'][1]:
                    resultado[anio]['mejor_pelicula'] = (lt.get_element(catalog['title'], i), calificacion)
                if calificacion < resultado[anio]['peor_pelicula'][1]:
                    resultado[anio]['peor_pelicula'] = (lt.get_element(catalog['title'], i), calificacion)
    
    return resultado


def req_7(catalog):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    resultado = {}
    for pelicula in catalog['peliculas']:
        anio = int(pelicula['release_date'].split('-')[0])
        if compania in pelicula['production_companies'] and anio_inicio <= anio <= anio_fin:
            if anio not in resultado:
                resultado[anio] = {
                    'total_peliculas': 0,
                    'total_duracion': 0,
                    'total_ganancias': 0,
                    'mejor_pelicula': ('', -float('inf')),
                    'peor_pelicula': ('', float('inf'))
                }
            resultado[anio]['total_peliculas'] += 1
            resultado[anio]['total_duracion'] += pelicula['runtime']
            resultado[anio]['total_ganancias'] += pelicula['revenue'] - pelicula['budget']
            if pelicula['vote_average'] > resultado[anio]['mejor_pelicula'][1]:
                resultado[anio]['mejor_pelicula'] = (pelicula['title'], pelicula['vote_average'])
            if pelicula['vote_average'] < resultado[anio]['peor_pelicula'][1]:
                resultado[anio]['peor_pelicula'] = (pelicula['title'], pelicula['vote_average'])

    return resultado


def req_8(catalog):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    resultado = {}
    for pelicula in catalog['peliculas']:
        anio = int(pelicula['release_date'].split('-')[0])
        if genero in pelicula['genres'] and anio >= anio_inicio:
            if anio not in resultado:
                resultado[anio] = {
                    'total_peliculas': 0,
                    'total_duracion': 0,
                    'total_ganancias': 0,
                    'mejor_pelicula': ('', -float('inf')),
                    'peor_pelicula': ('', float('inf'))
                }
            resultado[anio]['total_peliculas'] += 1
            resultado[anio]['total_duracion'] += pelicula['runtime']
            resultado[anio]['total_ganancias'] += pelicula['revenue'] - pelicula['budget']
            if pelicula['vote_average'] > resultado[anio]['mejor_pelicula'][1]:
                resultado[anio]['mejor_pelicula'] = (pelicula['title'], pelicula['vote_average'])
            if pelicula['vote_average'] < resultado[anio]['peor_pelicula'][1]:
                resultado[anio]['peor_pelicula'] = (pelicula['title'], pelicula['vote_average'])

    return resultado


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
