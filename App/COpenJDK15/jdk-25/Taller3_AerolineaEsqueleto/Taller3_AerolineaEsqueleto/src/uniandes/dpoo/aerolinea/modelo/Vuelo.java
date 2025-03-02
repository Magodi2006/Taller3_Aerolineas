package uniandes.dpoo.aerolinea.modelo;

import java.util.ArrayList;
import java.util.List;
import uniandes.dpoo.aerolinea.tiquetes.Tiquete;

/**
 * Representa un vuelo en la aerolínea.
 */
public class Vuelo {
    private String fecha;
    private Ruta ruta;
    private Avion avion;
    private boolean realizado;
    private List<Tiquete> tiquetes;

    public Vuelo(String fecha, Ruta ruta, Avion avion) {
        this.fecha = fecha;
        this.ruta = ruta;
        this.avion = avion;
        this.realizado = false;
        this.tiquetes = new ArrayList<>();
    }

    public String getFecha() {
        return fecha;
    }

    public Ruta getRuta() {
        return ruta;
    }

    public Avion getAvion() {
        return avion;
    }

    public boolean isRealizado() {
        return realizado;
    }

    public void setRealizado(boolean realizado) {
        this.realizado = realizado;
    }

    public List<Tiquete> getTiquetes() {
        return tiquetes;
    }

    public void agregarTiquete(Tiquete tiquete) {
        this.tiquetes.add(tiquete);
    }

    public int getCapacidadDisponible() {
        return avion.getCapacidad() - tiquetes.size();
    }
    public int getTarifaBase() {
        return 100000; 
    }

}
