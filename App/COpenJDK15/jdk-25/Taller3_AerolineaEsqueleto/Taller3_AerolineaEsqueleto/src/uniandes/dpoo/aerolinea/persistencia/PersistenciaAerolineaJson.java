package uniandes.dpoo.aerolinea.persistencia;

import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

import org.json.JSONArray;
import org.json.JSONObject;
import org.json.JSONTokener;

import uniandes.dpoo.aerolinea.exceptions.InformacionInconsistenteException;
import uniandes.dpoo.aerolinea.modelo.Aerolinea;
import uniandes.dpoo.aerolinea.modelo.Ruta;
import uniandes.dpoo.aerolinea.modelo.Avion;
import uniandes.dpoo.aerolinea.modelo.Vuelo;

/**
 * Clase que maneja la persistencia de la aerolínea en formato JSON.
 */
public class PersistenciaAerolineaJson implements IPersistenciaAerolinea {

    /**
     * Carga la información de la aerolínea desde un archivo JSON.
     */
    @Override
    public void cargarAerolinea(String archivo, Aerolinea aerolinea) throws IOException, InformacionInconsistenteException {
        try (FileReader reader = new FileReader(archivo)) {
            JSONTokener tokener = new JSONTokener(reader);
            JSONObject jsonObject = new JSONObject(tokener);

            // Cargar rutas
            JSONArray rutasArray = jsonObject.getJSONArray("rutas");
            for (int i = 0; i < rutasArray.length(); i++) {
                JSONObject rutaJson = rutasArray.getJSONObject(i);
                String codigoRuta = rutaJson.getString("codigo");
                String origen = rutaJson.getString("origen");
                String destino = rutaJson.getString("destino");

                Ruta ruta = new Ruta(codigoRuta, origen, destino);
                aerolinea.agregarRuta(ruta);
            }

            // Cargar aviones
            JSONArray avionesArray = jsonObject.getJSONArray("aviones");
            for (int i = 0; i < avionesArray.length(); i++) {
                JSONObject avionJson = avionesArray.getJSONObject(i);
                String matricula = avionJson.getString("matricula");
                int capacidad = avionJson.getInt("capacidad");

                Avion avion = new Avion(matricula, capacidad);
                aerolinea.agregarAvion(avion);
            }

            // Cargar vuelos
            JSONArray vuelosArray = jsonObject.getJSONArray("vuelos");
            for (int i = 0; i < vuelosArray.length(); i++) {
                JSONObject vueloJson = vuelosArray.getJSONObject(i);
                String fecha = vueloJson.getString("fecha");
                String codigoRuta = vueloJson.getString("codigoRuta");
                String matriculaAvion = vueloJson.getString("avion");

                Ruta ruta = aerolinea.getRuta(codigoRuta);
                Avion avion = aerolinea.getAvion(matriculaAvion);

                if (ruta == null || avion == null) {
                    throw new InformacionInconsistenteException("Error al cargar vuelo: Ruta o avión no encontrados.");
                }

                Vuelo vuelo = new Vuelo(fecha, ruta, avion);
                aerolinea.agregarVuelo(vuelo);
            }
        }
    }

    /**
     * Guarda la información de la aerolínea en un archivo JSON.
     */
    @Override
    public void salvarAerolinea(String archivo, Aerolinea aerolinea) throws IOException {
        JSONObject jsonObject = new JSONObject();

        // Guardar rutas
        JSONArray rutasArray = new JSONArray();
        for (Ruta ruta : aerolinea.getRutas()) {
            JSONObject rutaJson = new JSONObject();
            rutaJson.put("codigo", ruta.getCodigoRuta());
            rutaJson.put("origen", ruta.getOrigen());
            rutaJson.put("destino", ruta.getDestino());
            rutasArray.put(rutaJson);
        }
        jsonObject.put("rutas", rutasArray);

        // Guardar aviones
        JSONArray avionesArray = new JSONArray();
        for (Avion avion : aerolinea.getAviones()) {
            JSONObject avionJson = new JSONObject();
            avionJson.put("matricula", avion.getMatricula());
            avionJson.put("capacidad", avion.getCapacidad());
            avionesArray.put(avionJson);
        }
        jsonObject.put("aviones", avionesArray);

        // Guardar vuelos
        JSONArray vuelosArray = new JSONArray();
        for (Vuelo vuelo : aerolinea.getVuelos()) {
            JSONObject vueloJson = new JSONObject();
            vueloJson.put("fecha", vuelo.getFecha());
            vueloJson.put("codigoRuta", vuelo.getRuta().getCodigoRuta());
            vueloJson.put("avion", vuelo.getAvion().getMatricula());
            vuelosArray.put(vueloJson);
        }
        jsonObject.put("vuelos", vuelosArray);

        // Escribir en el archivo
        try (FileWriter writer = new FileWriter(archivo)) {
            writer.write(jsonObject.toString(4)); // 4 espacios para identación
        }
    }
}
