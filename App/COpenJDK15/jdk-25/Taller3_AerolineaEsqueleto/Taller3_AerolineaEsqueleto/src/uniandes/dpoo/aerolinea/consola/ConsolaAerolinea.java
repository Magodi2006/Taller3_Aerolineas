package uniandes.dpoo.aerolinea.consola;

import java.io.IOException;


import uniandes.dpoo.aerolinea.exceptions.InformacionInconsistenteException;
import uniandes.dpoo.aerolinea.modelo.Aerolinea;
import uniandes.dpoo.aerolinea.persistencia.CentralPersistencia;
import uniandes.dpoo.aerolinea.persistencia.TipoInvalidoException;
import uniandes.dpoo.aerolinea.modelo.Ruta;
import uniandes.dpoo.aerolinea.modelo.Avion;
import uniandes.dpoo.aerolinea.modelo.Vuelo;
import uniandes.dpoo.aerolinea.modelo.tarifas.CalculadoraTarifasTemporadaAlta;
import uniandes.dpoo.aerolinea.modelo.tarifas.CalculadoraTarifas;
import uniandes.dpoo.aerolinea.exceptions.TipoInvalidoException;
import uniandes.dpoo.aerolinea.exceptions.VueloSobrevendidoException;



public class ConsolaAerolinea extends ConsolaBasica
{
    private Aerolinea unaAerolinea;

    /**
     * Es un método que corre la aplicación y realmente no hace nada interesante: sólo muestra cómo se podría utilizar la clase Aerolínea para hacer pruebas.
     */
    
    public void correrAplicacion() {
    	try {
            unaAerolinea = new Aerolinea();
            unaAerolinea.setCalculadoraTarifas(new CalculadoraTarifasTemporadaAlta());

            // 🔹 Agregar la ruta manualmente
            Ruta ruta4558 = new Ruta("4558", "Bogotá", "Medellín");
            unaAerolinea.agregarRuta(ruta4558);
            System.out.println(" Ruta agregada: 4558 - Bogotá a Medellín");

            // 🔹 Agregar un avión para el vuelo
            Avion avion1 = new Avion("A320", 180);
            unaAerolinea.agregarAvion(avion1);
            System.out.println(" Avión agregado: A320 (180 pasajeros)");

            // 🔹 Agregar el vuelo antes de cargar los tiquetes
            Vuelo vuelo4558 = new Vuelo("2024-11-05", ruta4558, avion1);
            unaAerolinea.agregarVuelo(vuelo4558);
            System.out.println(" Vuelo agregado: 4558 en 2024-11-05");

            // 🔹 Cargar los tiquetes
            String archivo = "./datos/tiquetes.json";
            System.out.println("Cargando tiquetes desde: " + archivo);
            unaAerolinea.cargarTiquetes(archivo, CentralPersistencia.JSON);
            System.out.println("Tiquetes cargados correctamente.");

            // 🔹 PRUEBA: Venta de tiquetes
            System.out.println("\n Vendiendo tiquetes...");
            int totalVenta = unaAerolinea.venderTiquetes("Bob", "2024-11-05", "4558", 2);
            System.out.println(" Total venta: $" + totalVenta);

        } catch (TipoInvalidoException | IOException | InformacionInconsistenteException | VueloSobrevendidoException e) {
            e.printStackTrace();
        } catch (Exception e) {
            System.err.println(" ERROR en la venta de tiquetes: " + e.getMessage());
        }
    }

    
public static void main(String[] args) {
    ConsolaAerolinea ca = new ConsolaAerolinea();
    ca.correrAplicacion();
}
}

