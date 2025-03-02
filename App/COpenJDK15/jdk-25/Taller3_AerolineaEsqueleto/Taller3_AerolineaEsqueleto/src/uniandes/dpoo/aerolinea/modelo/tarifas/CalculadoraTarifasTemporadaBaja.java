package uniandes.dpoo.aerolinea.modelo.tarifas;

import uniandes.dpoo.aerolinea.modelo.cliente.Cliente;

/**
 * Implementación de CalculadoraTarifas para temporada baja.
 */
public class CalculadoraTarifasTemporadaBaja extends CalculadoraTarifas {
    
    /**
     * Reduce la tarifa base en un 10% durante la temporada baja.
     */
    @Override
    public int calcularTarifa(Cliente cliente, int tarifaBase) {
        return (int) (tarifaBase * 0.9);
    }
}

