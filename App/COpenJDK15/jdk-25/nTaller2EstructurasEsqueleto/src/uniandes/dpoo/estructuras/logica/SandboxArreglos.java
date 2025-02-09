package uniandes.dpoo.estructuras.logica;

import java.util.HashMap;
import java.util.Arrays;

/**
 * Esta clase tiene un conjunto de métodos para practicar operaciones sobre arreglos de enteros y de cadenas.
 *
 * Todos los métodos deben operar sobre los atributos arregloEnteros y arregloCadenas.
 * 
 * No pueden agregarse nuevos atributos.
 * 
 * Implemente los métodos usando operaciones sobre arreglos (ie., no haga cosas como construir listas para evitar la manipulación de arreglos).
 */
public class SandboxArreglos
{
    /**
     * Un arreglo de enteros para realizar varias de las siguientes operaciones.
     * 
     * Ninguna posición del arreglo puede estar vacía en ningún momento.
     */
    private int[] arregloEnteros;

    /**
     * Un arreglo de cadenas para realizar varias de las siguientes operaciones
     * 
     * Ninguna posición del arreglo puede estar vacía en ningún momento.
     */
    private String[] arregloCadenas;

    /**
     * Crea una nueva instancia de la clase con los dos arreglos inicializados pero vacíos (tamaño 0)
     */
    public SandboxArreglos( )
    {
        arregloEnteros = new int[]{};
        arregloCadenas = new String[]{};
    }

    /**
     * Retorna una copia del arreglo de enteros, es decir un nuevo arreglo del mismo tamaño que contiene copias de los valores del arreglo original
     * @return Una copia del arreglo de enteros
     */
    public int[] getCopiaEnteros( )
    {
        return arregloEnteros.clone();
    }

    /**
     * Retorna una copia del arreglo de cadenas, es decir un nuevo arreglo del mismo tamaño que contiene copias de los valores del arreglo original
     * @return Una copia del arreglo de cadenas
     */
    public String[] getCopiaCadenas( )
    {
        return arregloCadenas.clone();
    }

    /**
     * Retorna la cantidad de valores en el arreglo de enteros
     * @return
     */
    public int getCantidadEnteros( )
    {
        return arregloEnteros.length;
    }

    /**
     * Retorna la cantidad de valores en el arreglo de cadenas
     * @return
     */
    public int getCantidadCadenas( )
    {
        return arregloCadenas.length;
    }

    /**
     * Agrega un nuevo valor al final del arreglo. Es decir que este método siempre debería aumentar en 1 la capacidad del arreglo.
     * 
     * @param entero El valor que se va a agregar.
     */
    public void agregarEntero( int entero )
    {
    	 // Crear un nuevo arreglo con un tamaño mayor
        int[] nuevoArreglo = new int[arregloEnteros.length + 1];

        // Copiar los valores del arreglo original
        System.arraycopy(arregloEnteros, 0, nuevoArreglo, 0, arregloEnteros.length);

        // Agregar el nuevo valor al final
        nuevoArreglo[nuevoArreglo.length - 1] = entero;

        // Asignar el nuevo arreglo al atributo de la clase
        arregloEnteros = nuevoArreglo;

    }

    /**
     * Agrega un nuevo valor al final del arreglo. Es decir que este método siempre debería aumentar en 1 la capacidad del arreglo.
     * 
     * @param cadena La cadena que se va a agregar.
     */
    public void agregarCadena( String cadena )
    {
    	String[] nuevoArreglo = new String[arregloCadenas.length + 1];
        System.arraycopy(arregloCadenas, 0, nuevoArreglo, 0, arregloCadenas.length);
        nuevoArreglo[nuevoArreglo.length - 1] = cadena;
        arregloCadenas = nuevoArreglo;

    }

    /**
     * Elimina todas las apariciones de un determinado valor dentro del arreglo de enteros
     * @param valor El valor que se va eliminar
     */
    public void eliminarEntero( int valor )
    {
    	int count = 0;

        // Contar cuántas veces aparece el valor a eliminar
        for (int num : arregloEnteros) {
            if (num == valor) count++;
        }

        // Si no hay elementos a eliminar, salir del método
        if (count == 0) {
            return;
        }

        // Crear un nuevo arreglo con el tamaño ajustado
        int[] nuevoArreglo = new int[arregloEnteros.length - count];
        int index = 0;

        // Copiar los valores que NO sean el valor a eliminar
        for (int num : arregloEnteros) {
            if (num != valor) {
                nuevoArreglo[index++] = num;
            }
        }

        // Verificar si el nuevo tamaño es correcto antes de asignarlo
        if (index == nuevoArreglo.length) {
            arregloEnteros = nuevoArreglo;
        } else {
            System.out.println("Error: No se eliminaron los valores correctamente.");
        }

    }

    /**
     * Elimina todas las apariciones de un determinado valor dentro del arreglo de cadenas
     * @param cadena La cadena que se va eliminar
     */
    public void eliminarCadena( String cadena )
    {
    	 int count = 0;
    	    
    	    // Contar cuántas veces aparece la cadena a eliminar
    	    for (String str : arregloCadenas) {
    	        if (str.equals(cadena)) count++;
    	    }

    	    // Si no hay elementos a eliminar, salir del método
    	    if (count == 0) {
    	        return;
    	    }

    	    // Crear un nuevo arreglo con el tamaño ajustado
    	    String[] nuevoArreglo = new String[arregloCadenas.length - count];
    	    int index = 0;

    	    // Copiar los valores que NO sean la cadena a eliminar
    	    for (String str : arregloCadenas) {
    	        if (!str.equals(cadena)) {
    	            nuevoArreglo[index++] = str;
    	        }
    	    }

    	 // Verificar si el nuevo tamaño es correcto antes de asignarlo
    	    if (index == nuevoArreglo.length) {
    	        arregloCadenas = nuevoArreglo;
    	    } else {
    	        System.out.println("Error: No se eliminaron las cadenas correctamente.");
    	    }
    }

    /**
     * Inserta un nuevo entero en el arreglo de enteros.
     * 
     * @param entero El nuevo valor que debe agregarse
     * @param posicion La posición donde debe quedar el nuevo valor en el arreglo aumentado. Si la posición es menor a 0, se inserta el valor en la primera posición. Si la
     *        posición es mayor que el tamaño del arreglo, se inserta el valor en la última posición.
     */
    public void insertarEntero( int entero, int posicion )
    {
    	// Validar la posición
        if (posicion < 0) posicion = 0;
        if (posicion > arregloEnteros.length) posicion = arregloEnteros.length;

        // Crear un nuevo arreglo con un espacio extra
        int[] nuevoArreglo = new int[arregloEnteros.length + 1];

        // Copiar los elementos hasta la posición deseada
        System.arraycopy(arregloEnteros, 0, nuevoArreglo, 0, posicion);

        // Insertar el nuevo valor en la posición correcta
        nuevoArreglo[posicion] = entero;

        // Copiar los elementos restantes
        System.arraycopy(arregloEnteros, posicion, nuevoArreglo, posicion + 1, arregloEnteros.length - posicion);

        // Asignar el nuevo arreglo a la variable de clase
        arregloEnteros = nuevoArreglo;

    }

    /**
     * Elimina un valor del arreglo de enteros dada su posición.
     * @param posicion La posición donde está el elemento que debe ser eliminado. Si el parámetro posicion no corresponde a ninguna posición del arreglo de enteros, el método
     *        no debe hacer nada.
     */
    public void eliminarEnteroPorPosicion( int posicion )
    {
    	// Verificar si la posición es válida
        if (posicion < 0 || posicion >= arregloEnteros.length) {
            return; // No hacer nada si la posición es inválida
        }

        // Crear un nuevo arreglo con un tamaño menor
        int[] nuevoArreglo = new int[arregloEnteros.length - 1];

        // Copiar los elementos antes de la posición
        System.arraycopy(arregloEnteros, 0, nuevoArreglo, 0, posicion);

        // Copiar los elementos después de la posición
        System.arraycopy(arregloEnteros, posicion + 1, nuevoArreglo, posicion, arregloEnteros.length - posicion - 1);

        // Asignar el nuevo arreglo al atributo
        arregloEnteros = nuevoArreglo;

    }

    /**
     * Reinicia el arreglo de enteros con los valores contenidos en el arreglo del parámetro 'valores' truncados.
     * 
     * Es decir que si el valor fuera 3.67, en el nuevo arreglo de enteros debería quedar el entero 3.
     * @param valores Un arreglo de valores decimales.
     */
    public void reiniciarArregloEnteros( double[] valores )
    {
    	// Crear un nuevo arreglo con el tamaño adecuado
        arregloEnteros = new int[valores.length];

        // Truncar los valores y asignarlos al nuevo arreglo
        for (int i = 0; i < valores.length; i++) {
            arregloEnteros[i] = (int) valores[i]; // Convierte el valor a entero truncando
        }


    }

    /**
     * Modifica el arreglo de enteros para que todos los valores sean positivos.
     * 
     * Es decir que si en una posición había un valor negativo, después de ejecutar el método debe quedar el mismo valor muliplicado por -1.
     */
    public void volverPositivos( )
    {
    	 for (int i = 0; i < arregloEnteros.length; i++) {
    	        if (arregloEnteros[i] < 0) {
    	            arregloEnteros[i] *= -1; // Convierte el número negativo en positivo
    	        }
    	    }

    }

    /**
     * Modifica el arreglo de enteros para que todos los valores queden organizados de menor a mayor.
     */
    
    public void organizarEnteros( )
    {
    	 Arrays.sort(arregloEnteros);

    }

    /**
     * Modifica el arreglo de cadenas para que todos los valores queden organizados lexicográficamente.
     */
    public void organizarCadenas( )
    {
    	Arrays.sort(arregloCadenas);

    }

    /**
     * Cuenta cuántas veces aparece el valor recibido por parámetro en el arreglo de enteros
     * @param valor El valor buscado
     * @return La cantidad de veces que aparece el valor
     */
    public int contarApariciones( int valor )
    {
    	int count = 0;
        for (int num : arregloEnteros) {
            if (num == valor) count++;
        }
        return count;
    }

    /**
     * Cuenta cuántas veces aparece la cadena recibida por parámetro en el arreglo de cadenas.
     * 
     * La búsqueda no debe diferenciar entre mayúsculas y minúsculas.
     * @param cadena La cadena buscada
     * @return La cantidad de veces que aparece la cadena
     */
    public int contarApariciones( String cadena )
    {
    	int count = 0;
        for (String str : arregloCadenas) {
            if (str.equalsIgnoreCase(cadena)) {
                count++;
            }
        }
        return count;
    }

    /**
     * Busca en qué posiciones del arreglo de enteros se encuentra el valor que se recibe en el parámetro
     * @param valor El valor que se debe buscar
     * @return Un arreglo con los números de las posiciones del arreglo de enteros en las que se encuentra el valor buscado. Si el valor no se encuentra, el arreglo retornado
     *         es de tamaño 0.
     */
    public int[] buscarEntero( int valor )
    {
    	int count = contarApariciones(valor);
        int[] posiciones = new int[count];

        int index = 0;
        for (int i = 0; i < arregloEnteros.length; i++) {
            if (arregloEnteros[i] == valor) {
                posiciones[index++] = i;
            }
        }
        return posiciones;
    }

    /**
     * Calcula cuál es el rango de los enteros (el valor mínimo y el máximo).
     * @return Un arreglo con dos posiciones: en la primera posición, debe estar el valor mínimo en el arreglo de enteros; en la segunda posición, debe estar el valor máximo
     *         en el arreglo de enteros. Si el arreglo está vacío, debe retornar un arreglo vacío.
     */
    public int[] calcularRangoEnteros( )
    {
    	if (arregloEnteros.length == 0) {
            return new int[0]; // Retorna un arreglo vacío si no hay elementos
        }

        int min = arregloEnteros[0];
        int max = arregloEnteros[0];

        for (int num : arregloEnteros) {
            if (num < min) {
                min = num;
            }
            if (num > max) {
                max = num;
            }
        }

        return new int[]{min, max}; // Retorna el mínimo y el máximo en un arreglo de tamaño 2

    }

    /**
     * Calcula un histograma de los valores del arreglo de enteros y lo devuelve como un mapa donde las llaves son los valores del arreglo y los valores son la cantidad de
     * veces que aparece cada uno en el arreglo de enteros.
     * @return Un mapa con el histograma de valores.
     */
    public HashMap<Integer, Integer> calcularHistograma( )
    {
    	HashMap<Integer, Integer> histograma = new HashMap<>();
        
        for (int num : arregloEnteros) {
            histograma.put(num, histograma.getOrDefault(num, 0) + 1);
        }
        
        return histograma;
    }

    /**
     * Cuenta cuántos valores dentro del arreglo de enteros están repetidos.
     * @return La cantidad de enteos diferentes que aparecen más de una vez
     */
    public int contarEnterosRepetidos( )
    {
    	HashMap<Integer, Integer> frecuencia = new HashMap<>();
        
        // Contar la frecuencia de cada número
        for (int num : arregloEnteros) {
            frecuencia.put(num, frecuencia.getOrDefault(num, 0) + 1);
        }

        // Contar cuántos valores tienen frecuencia mayor a 1
        int repetidos = 0;
        for (int count : frecuencia.values()) {
            if (count > 1) {
                repetidos++;
            }
        }
        
        return repetidos;
    }

    /**
     * Compara el arreglo de enteros con otro arreglo de enteros y verifica si son iguales, es decir que contienen los mismos elementos exactamente en el mismo orden.
     * @param otroArreglo El arreglo de enteros con el que se debe comparar
     * @return True si los arreglos son idénticos y false de lo contrario
     */
    public boolean compararArregloEnteros( int[] otroArreglo )
    {
    	return Arrays.equals(arregloEnteros, otroArreglo);
    }

    /**
     * Compara el arreglo de enteros con otro arreglo de enteros y verifica que tengan los mismos elementos, aunque podría ser en otro orden.
     * @param otroArreglo El arreglo de enteros con el que se debe comparar
     * @return True si los elementos en los dos arreglos son los mismos
     */
    public boolean mismosEnteros( int[] otroArreglo )
    {
    	if (arregloEnteros.length != otroArreglo.length) {
            return false;
        }

        int[] copiaArreglo = arregloEnteros.clone();
        int[] copiaOtro = otroArreglo.clone();

        Arrays.sort(copiaArreglo);
        Arrays.sort(copiaOtro);

        return Arrays.equals(copiaArreglo, copiaOtro);
    }

    /**
     * Cambia los elementos del arreglo de enteros por una nueva serie de valores generada de forma aleatoria.
     * 
     * Para generar los valores se debe partir de una distribución uniforme usando Math.random().
     * 
     * Los números en el arreglo deben quedar entre el valor mínimo y el máximo.
     * @param cantidad La cantidad de elementos que debe haber en el arreglo
     * @param minimo El valor mínimo para los números generados
     * @param maximo El valor máximo para los números generados
     */
    public void generarEnteros( int cantidad, int minimo, int maximo )
    {
    	arregloEnteros = new int[cantidad];
        for (int i = 0; i < cantidad; i++) {
            arregloEnteros[i] = (int) (Math.random() * (maximo - minimo + 1)) + minimo;
        }

    }
    
    public void reiniciarArregloCadenas(Object[] objetos) {
        arregloCadenas = new String[objetos.length];
        for (int i = 0; i < objetos.length; i++) {
            arregloCadenas[i] = objetos[i].toString();
        }
    } 
    
}

	

	
		

