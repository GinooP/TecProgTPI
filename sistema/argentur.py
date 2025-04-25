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

    #Muestra la informacion de todos los servicios registrados en la lista de servicios. (Inciso 1)
    def consultarServicios(self):
        stringFinal=[]
        for servicio in self._servicios:
            stringFinal.append(f"{servicio.informacionServicio()}")
        return "\n\n".join(stringFinal)
    