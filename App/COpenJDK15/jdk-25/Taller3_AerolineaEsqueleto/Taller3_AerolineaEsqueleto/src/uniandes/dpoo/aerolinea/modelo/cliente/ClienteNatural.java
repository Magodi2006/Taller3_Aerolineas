package uniandes.dpoo.aerolinea.modelo.cliente;

/**
 * Representa a un cliente natural en la aerolínea.
 */
public class ClienteNatural extends Cliente {
    public static final String NATURAL = "NATURAL";  // 🔹 Debe estar en mayúsculas

    public ClienteNatural(String nombre) {
        super(nombre);
    }

    @Override
    public String getIdentificador() {
        return nombre;
    }

    @Override
    public String getTipoCliente() {
        return NATURAL;
    }
}
