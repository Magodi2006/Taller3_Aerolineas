package uniandes.dpoo.aerolinea.modelo;

public class Avion {
	 private String matricula;
	    private int capacidad;

	    public Avion(String matricula, int capacidad) {
	        this.matricula = matricula;
	        this.capacidad = capacidad;
	    }

	    public String getMatricula() {
	        return matricula;
	    }

	    public int getCapacidad() {
	        return capacidad;
	    }

}
