from modelos.servicio import Servicio
from modelos.venta import Venta

class Argentur:
    # La empresa tiene un estado(está activo o no) y muchos servicios y ¿¿ pasajeros ??
    def __init__(self, sistema_activo:bool, ventas:list[Venta], servicios:list[Servicio]):
        self._sistema_activo = sistema_activo
        # Relaciones
        self._ventas = ventas
        self._servicios = servicios

    def agregarServicio(self, servicio:Servicio):
        self._servicios.append(servicio)