from modelos.servicio import Servicio
from modelos.venta import Venta
from modelos.pasajero import Pasajero

class Argentur:
    # La empresa tiene un estado(está activo o no) y muchos servicios y ¿¿ pasajeros ??
    def __init__(self, sistema_activo:bool, ventas:list[Venta], servicios:list[Servicio]):
        self._sistema_activo = sistema_activo
        # Relaciones
        self._ventas = ventas
        self._servicios = servicios

    def cambiarEstadoSistema(self):
        self._sistema_activo = not self._sistema_activo

    def agregarServicio(self, servicio:Servicio):
        self._servicios.append(servicio)

        #Muestra la informacion de todos los servicios registrados en la lista de servicios. (Inciso 1)
    def consultarServicios(self):
        stringFinal=[]
        for servicio in self._servicios:
            stringFinal.append(f"{servicio.informacionServicio()}")
        return "\n\n".join(stringFinal)
    
    
    def buscarServicioPorId(self, id_servicio):
        for servicio in self._servicios:
            if servicio.id == id_servicio:
                return servicio
        return None


    def simularReserva(self):
        self.consultarServicios() # Consulto los servicios disponibles
        idServicio = int(input("Ingrese el id del servicio: ")) # El usuario(o pasajero) selecciona un servicio ingresando el id
        servicio = self.buscarServicioPorId(idServicio) # Busco el servicio por id
        if servicio:
            print(servicio.listaAsientosDisponibles()) # si fue encontrado, listo los asientos disponibles
        else:
            print(f"El servicio no fue encontrado.")# No fue encontrado el servicio. ID erroneo
            

