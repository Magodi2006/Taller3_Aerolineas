package uniandes.dpoo.aerolinea.modelo.tarifas;

import uniandes.dpoo.aerolinea.modelo.cliente.Cliente;

/**
 * Clase abstracta para calcular tarifas de vuelos.
 */
public abstract class CalculadoraTarifas {
    
    /**
     * Calcula el costo del tiquete para un cliente específico.
     * @param cliente Cliente que comprará el tiquete.
     * @param tarifaBase Tarifa base del vuelo.
     * @return Tarifa final ajustada según la temporada.
     */
    public abstract int calcularTarifa(Cliente cliente, int tarifaBase);
}
