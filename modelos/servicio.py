from unidad import Unidad
from itinerario import Itinerario
from venta import Venta
from reserva import Reserva
from datetime import datetime

class Servicio:

    def __init__(self,id_servicio:int, unidad:Unidad, fecha_partida:datetime, fecha_llegada:datetime, calidad:str, precio:float, itinerario:Itinerario, reservas:list[Reserva], ventas:list[Venta]):
        # atributos de la clase
        self._id_servicio = id_servicio
        self._fecha_partida = fecha_partida
        self._fecha_llegada = fecha_llegada
        self._calidad = calidad
        self._precio = precio
        # un servicio tiene asociada una unidad, un itinerario para esa unidad, muchas reservas y ventas realizadas por pasajeros
        self._unidad = unidad
        self._itinerario = itinerario
        self._reservas = reservas
        self._ventas = ventas

    def listarAsientosDisponibles(self):
        return self._unidad.listarAsientosDisponibles()
        
    def verPrecio(self):
        return self._precio
    
    def verItinerarioDestino(self):
        return self._itinerario.verCiudadDestino()
    
    # mostrar montos totales facturados en ese periodo
    def totalPorPeriodo(self,fecha_desde:datetime, fecha_hasta:datetime):
        total = 0
        for venta in self._ventas:
            if venta.verFecha() >= fecha_desde and venta.verFecha() <= fecha_hasta:
                total += self._precio
        return float(total)
    
    def verVentas(self):
        return self._ventas