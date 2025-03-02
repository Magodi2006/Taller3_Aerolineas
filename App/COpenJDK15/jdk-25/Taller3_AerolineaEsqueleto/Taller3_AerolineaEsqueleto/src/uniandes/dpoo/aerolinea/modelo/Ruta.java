package uniandes.dpoo.aerolinea.modelo;

/**
 * Representa una ruta en la aerolínea.
 */
public class Ruta {
    private String codigoRuta;
    private String origen;
    private String destino;

    public Ruta(String codigoRuta, String origen, String destino) {
        this.codigoRuta = codigoRuta;
        this.origen = origen;
        this.destino = destino;
    }

    public String getCodigoRuta() {
        return codigoRuta;
    }

    public String getOrigen() {
        return origen;
    }

    public String getDestino() {
        return destino;
    }
}
