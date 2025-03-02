package uniandes.dpoo.aerolinea.modelo.cliente;

import org.json.JSONObject;

/**
 * Esta clase se usa para representar a los clientes de la aerolínea que son empresas
 */
public class ClienteCorporativo extends Cliente{
	 private String nombreEmpresa;
	    private int tamanoEmpresa;
	    public static final String CORPORATIVO = "CORPORATIVO";

	    /**
	     * Constructor de ClienteCorporativo
	     * @param nombreEmpresa Nombre de la empresa
	     * @param tamanoEmpresa Tamaño de la empresa
	     */
	    public ClienteCorporativo(String nombreEmpresa, int tamanoEmpresa) {
	        super(nombreEmpresa);
	        this.nombreEmpresa = nombreEmpresa;
	        this.tamanoEmpresa = tamanoEmpresa;
	    }

	    @Override
	    public String getIdentificador() {
	        return nombreEmpresa;
	    }

	    @Override
	    public String getTipoCliente() {
	        return CORPORATIVO;
	    }
	
    
	    public static ClienteCorporativo cargarDesdeJSON(org.json.JSONObject cliente) {
	        if (!cliente.has("nombreEmpresa")) {
	            throw new org.json.JSONException("Error: ClienteCorporativo sin 'nombreEmpresa'. Verifica el JSON.");
	        }
	        if (!cliente.has("tamanoEmpresa")) {
	            throw new org.json.JSONException("Error: ClienteCorporativo sin 'tamanoEmpresa'. Verifica el JSON.");
	        }

	        String nombreEmpresa = cliente.getString("nombreEmpresa");
	        int tam = cliente.getInt("tamanoEmpresa");

	        return new ClienteCorporativo(nombreEmpresa, tam);
    }

    /**
     * Salva este objeto de tipo ClienteCorporativo dentro de un objeto JSONObject para que ese objeto se almacene en un archivo
     * @return El objeto JSON con toda la información del cliente corporativo
     */
    public JSONObject salvarEnJSON( ){
    	org.json.JSONObject jobject = new org.json.JSONObject();
        jobject.put("nombreEmpresa", this.nombreEmpresa);
        jobject.put("tamanoEmpresa", this.tamanoEmpresa);
        jobject.put("tipo", CORPORATIVO);
        return jobject;
    }
}

