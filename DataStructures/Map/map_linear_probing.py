from DataStructures.List import array_list as lt
from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf
import random as rd
def default_compare(key, element):
    """
    Función de comparación por defecto. Compara una llave con la llave de un elemento llave-valor.

    Parameters:
    key (any) - Llave a comparar
    element (map_entry) - entry a comparar

    Returns:
    0 si son iguales, 1 si key > la llave del element, -1 si key < que la llave del element

    Return type:
    int
    """
    element_key = me.get_key(element)
    
    if element_key is None:
        return 1  
    elif key == element_key:
        return 0
    elif key > element_key:
        return 1
    else:
        return -1

cmp_function = default_compare

def new_map(num_elements, load_factor, prime=109345121):
    """
    Crea una tabla de simbolos (map) sin elementos
    Se crea una tabla de simbolos (map) sin elementos con los siguientes atributos:
        prime: Número primo utilizado en la función hash
        capacity: Tamaño de la tabla. Siguiente número primo mayor a num_elements/load_factor
        scale: Número aleatorio entre 1 y prime-1
        shift: Número aleatorio entre 0 y prime-1
        table: Lista de tamaño capacity con las entradas de la tabla
        current_factor: Factor de carga actual de la tabla, inicializado en 0
        limit_factor: Factor de carga máximo de la tabla (load_factor)
        size: Número de elementos en la tabla
        type: Tipo de tabla (PROBING)

    Parameters:
    num_elements (int) - Número de parejas <key,value> que inicialmente puede almacenar la tabla
    load_factor (float) - Factor de carga máximo de la tabla
    prime (int) - Número primo utilizado en la función hash. Se utiliza 109345121 por defecto

    Returns:
    Un nuevo map

    Return type:
    map_linear_probing
    """
    capacity = mf.next_prime(num_elements//load_factor)
    scale = rd.randint(1,prime-1)
    shift = rd.randint(0, prime-1)
    hashtable = {"prime":prime,
                 "capacity":capacity,
                 "scale":scale,
                 "shift":shift,
                 "table":None,
                 "current_factor":0,
                 "limit_factor":load_factor,
                 "size":0,
                 "type": "PROBING"}
    hashtable["table"] = lt.new_list()
    for _ in range(capacity):
        entry = me.new_map_entry(None, None)
        lt.add_last(hashtable["table"], entry)
    return hashtable

def put(my_map, key, value):
    """
    Ingresa una pareja llave,valor a la tabla de hash. Si la llave ya existe en la tabla, se reemplaza el valor

    Parameters:
    my_map (map_linear_probing) - El map a donde se guarda la pareja llave-valor
    key (any) - la llave asociada a la pareja
    value (any) - el valor asociado a la pareja

    Returns:
    El map

    Return type:
    map_linear_probing
    """
    hash_value = mf.hash_value(my_map, key)
    occupied, slot = find_slot(my_map, key, hash_value)
    
    if not occupied:
        my_map["size"] += 1
        my_map["current_factor"] = my_map["size"] / my_map["capacity"]
    
    me.set_key(lt.get_element(my_map["table"], slot), key)
    me.set_value(lt.get_element(my_map["table"], slot), value)
    
    if my_map["current_factor"] > my_map["limit_factor"]:
        rehash(my_map)

    return my_map

def contains(my_map, key):
    """
    Valida si la llave key se encuentra en el map

    Retorna True si la llave key se encuentra en el my_map o False en caso contrario.

    Parameters:
    my_map (map_linear_probing) - El my_map a donde se guarda la pareja
    key (any) - la llave asociada a la pareja

    Returns:
    True si la llave se encuentra en el map, False en caso contrario

    Return type:
    bool
    """
    hash_value = mf.hash_value(my_map, key)
    occupied, _ = find_slot(my_map, key, hash_value)
    return occupied

def get(my_map, key):
    """
    Retorna el valor asociado a la llave key en el map

    Parameters:
    my_map (map_linear_probing) - Map a examinar
    key (any) - Llave a buscar

    Returns:
    Valor asociado a la llave key

    Return type:
    any
    """
    hash_value = mf.hash_value(my_map, key)
    occupied, slot = find_slot(my_map, key, hash_value)
    
    if occupied:
        return me.get_value(lt.get_element(my_map["table"], slot))
    return None

def remove(my_map, key):
    """
    Elimina la pareja llave-valor del map

    Parameters:
    my_map (map_linear_probing) - El map a examinar
    key (any) - Llave a eliminar

    Returns:
    El map sin la llave key

    Return type:
    map_linear_probing
    """
    hash_value = mf.hash_value(my_map, key)
    occupied, slot = find_slot(my_map, key, hash_value)
    
    if occupied:
        me.set_key(lt.get_element(my_map["table"], slot), "__EMPTY__")
        me.set_value(lt.get_element(my_map["table"], slot), "__EMPTY__")
        my_map["size"] -= 1
        my_map["current_factor"] = my_map["size"] / my_map["capacity"]

    return my_map

def size(my_map):
    """
    Retorna el número de parejas llave-valor en el map

    Parameters:
    my_map (map_linear_probing) - El map a examinar

    Returns:
    Número de parejas llave-valor en el map

    Return type:
    int
    """
    return my_map["size"]

def is_empty(my_map):
    """
    Indica si el map se encuentra vacío

    Parameters:
    my_map (map_linear_probing) - El map a examinar

    Returns:
    True si el map está vacío, False en caso contrario

    Return type:
    bool
    """
    return my_map["size"] == 0

def key_set(my_map):
    """
    Retorna una lista con todas las llaves de la tabla de hash

    Parameters:
    my_map (map_linear_probing) - El map a examinar

    Returns:
    lista de llaves

    Return type:
    array_list
    """
    keys = lt.new_list()
    
    for i in range(my_map['capacity']):
        entry = lt.get_element(my_map['table'], i)
        if me.get_key(entry) is not None and me.get_key(entry) != "__EMPTY__":
            lt.add_last(keys, me.get_key(entry))
            
    return keys

def value_set(my_map):
    """
    Retorna una lista con todos los valores de la tabla de hash

    Parameters:
    my_map (map_linear_probing) - El map a examinar

    Returns:
    lista de valores

    Return type:
    array_list
    """
    values = lt.new_list()
    
    for i in range(my_map['capacity']):
        entry = lt.get_element(my_map['table'], i)
        if me.get_value(entry) is not None and me.get_key(entry) != "__EMPTY__":
            lt.add_last(values, me.get_value(entry))
            
    return values

def find_slot(my_map, key, hash_value):
    """
    Busca la key a partir de una posición dada en la tabla.
    Utiliza la función de hash para encontrar la posición inicial de la llave. 
    Si la posición está ocupada, busca la siguiente posición disponible.
    Usa la función de comparación (default_compare) para determinar si la llave ya existe en la tabla.

    Parameters:
    my_map (map_linear_probing) - El map a examinar

    key (any) - Llave a buscar

    hash_value (int) - Posición inicial de la llave

    Returns:
    Retorna una tupla con dos valores. 
    El primero indica si la posición está ocupada, True si se encuentra la key de lo contrario False. 
    El segundo la posición en la tabla de hash donde se encuentra o posición libre para agregarla

    Return type:
    bool, int
    """
    first_avail = None
    found = False
    ocupied = False
    
    while not found:
        if is_available(my_map["table"], hash_value):
            if first_avail is None:
                first_avail = hash_value
            entry = lt.get_element(my_map["table"], hash_value)
            if me.get_key(entry) is None:
                found = True
        elif cmp_function(key, lt.get_element(my_map["table"], hash_value)) == 0:
            first_avail = hash_value
            found = True
            ocupied = True
        
        hash_value = (hash_value + 1) % my_map["capacity"]
        
    return ocupied, first_avail
            

def is_available(table, pos):
    """
    Informa si la posición pos está disponible en la tabla de hash.
    Se entiende que una posición está disponible si su contenido es igual a None (no se ha usado esa posición) o a __EMPTY__ (la posición fue liberada)

    Parameters:
    table (array_list) - Tabla de hash, implementada como una lista (array_list)

    pos (int) - Posición a verificar

    Returns:
    True si la posición está disponible, False en caso contrario

    Return type:
    bool
    """
    entry = lt.get_element(table, pos)
    if me.get_key(entry) is None or me.get_key(entry) == "__EMPTY__":
        return True
    return False

def rehash(my_map):
    """
    Hace rehash de todos los elementos de la tabla de hash.
    Incrementa la capacidad de la tabla al doble y se hace rehash de todos los elementos de la tabla uno por uno.
    Se utiliza la función hash_value para calcular el nuevo hash de cada llave.

    Parameters:
    my_map (map_linear_probing) - El map a hacer rehash

    Returns:
    El map con la nueva capacidad

    Return type:
    map_linear_probing
    """
    old_table = my_map['table']
    new_capacity = mf.next_prime(2 * my_map['capacity'])
    
    new_map = {
        'prime': my_map['prime'],
        'capacity': new_capacity,
        'scale': rd.randint(1, my_map['prime'] - 1), 
        'shift': rd.randint(0, my_map['prime'] - 1),  
        'table': lt.new_list(),
        'current_factor': 0,
        'limit_factor': my_map['limit_factor'],
        'size': 0,
        'type': my_map['type']
    }
    
    for _ in range(new_capacity):
        entry = me.new_map_entry(None, None)
        lt.add_last(new_map["table"], entry)

    for i in range(my_map['capacity']):
       entry = lt.get_element(old_table, i)
       
       if me.get_key(entry) is not None and me.get_key(entry) != "__EMPTY__":
           put(new_map, me.get_key(entry), me.get_value(entry))

    my_map['table'] = new_map["table"]
    my_map['capacity'] = new_capacity
    my_map['current_factor'] = my_map['size'] / new_capacity

    return my_map
