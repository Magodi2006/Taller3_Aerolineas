package uniandes.dpoo.aerolinea.modelo.cliente;

public abstract class Cliente {
	 protected String nombre;

	    public Cliente(String nombre) {
	        this.nombre = nombre;
	    }

	    /**
	     * Obtiene el identificador único del cliente.
	     * @return Identificador del cliente (puede ser nombre o empresa).
	     */
	    public abstract String getIdentificador();

	    /**
	     * Obtiene el tipo de cliente (NATURAL o CORPORATIVO).
	     * @return Tipo de cliente.
	     */
	    public abstract String getTipoCliente();

}
