from modelos.servicio import Servicio
from modelos.venta import Venta
from modelos.pasajero import Pasajero
from modelos.reserva import Reserva
import datetime

class Argentur:
    # La empresa tiene un estado(está activo o no) y muchos servicios y ¿¿ pasajeros ??
    def __init__(self, sistema_activo:bool, ventas:list[Venta], servicios:list[Servicio]):
        self._sistema_activo = sistema_activo
        # Relaciones
        self._ventas = ventas
        self._servicios = servicios

    def agregarServicio(self, servicio:Servicio):
        self._servicios.append(servicio)

    def consultarServicios():
        ...

    def buscarSservicioPorId(self, id_servicio):
        for servicio in self._servicios:
            if servicio.id == id_servicio:
                return servicio
        return None

    def seleccionarAsiento(self, servicio:Servicio, fecha_res:datetime):
        idAsiento=int(input("Ingrese el id del asiento: "))
        asiento=servicio.buscarAsiento(idAsiento)
        if asiento:
            nombre=str(input("Ingrese su nombre: "))
            dni=int(input("Ingrese nro de documento: "))
            mail=str(input("Ingrese su correo electrónico: "))
            reserva=servicio.agregarReserva(Pasajero(nombre,mail,dni,asiento),fecha_res)
            return reserva
        else:
            #error, no fue encontrado
            return False

    def mostrarReserva(self, reserva, fecha:datetime):
        print(f"Reserva realizada.{reserva.getPasajero()}"
            f"reserva del {fecha}")
    
    def simularReserva(self,fecha_reserva:datetime):
        self.consultarServicios() # Consulto los servicios disponibles
        idServicio = int(input("Ingrese el id del servicio: ")) # El usuario(o pasajero) selecciona un servicio ingresando el id
        servicio = self.buscarServicioPorId(idServicio) # Busco el servicio por id
        if servicio:
            #return servicio.listarAsientosDisponibles() # si fue encontrado, listo los asientos disponibles
            reserva=self.seleccionarAsiento(servicio,fecha_reserva)
            self.mostrarReserva(reserva,fecha_reserva)
        else:
            return None # No fue encontrado el servicio. ID erroneo