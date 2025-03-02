package uniandes.dpoo.aerolinea.modelo.tarifas;

import uniandes.dpoo.aerolinea.modelo.cliente.Cliente;

/**
 * Implementación de CalculadoraTarifas para temporada alta.
 */
public class CalculadoraTarifasTemporadaAlta extends CalculadoraTarifas {
    
    /**
     * Aumenta la tarifa base en un 20% durante la temporada alta.
     */
    @Override
    public int calcularTarifa(Cliente cliente, int tarifaBase) {
        return (int) (tarifaBase * 1.2);
    }
}
