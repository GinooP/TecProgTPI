import datetime
from modelos.servicio import Servicio
from modelos.venta import Venta
from modelos.pasajero import Pasajero

class Argentur:
    # La empresa tiene un estado(está activo o no) y muchos servicios y ¿¿ pasajeros ??
    # def __init__(self, sistema_activo:bool, ventas:list[Venta], servicios:list[Servicio]): con la relacion de venta
    def __init__(self, sistema_activo:bool, servicios:list[Servicio]):
        self._sistema_activo = sistema_activo
        # Relaciones
        # self._ventas = ventas
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
        
          
    def informe(self, fecha_desde:datetime, fecha_hasta:datetime):
        # mostrar montos totales facturados en ese periodo 
        total = 0
        for servicio in self._servicios:
            total += servicio.totalPorPeriodo(fecha_desde,fecha_hasta)
        
        # cantidad de viajes a cada localidad destino en ese periodo
        destinos_en_periodo = []
        # guardo todos los destinos en una lista en ese periodo
        for servicio in self._servicios:
            destino = servicio.verItinerarioDestino()
            for venta in servicio.verVentas():
                if venta.verFecha() >= fecha_desde and venta.verFecha() <= fecha_hasta:
                    destinos_en_periodo.append(destino)
        
        conteo = []
        for destino in destinos_en_periodo:
            encontrado = False
            for i in range(len(conteo)):
                if conteo[i][0] == destino:
                    conteo[i] = (destino,conteo[i][1] +1 )
                    encontrado = True
                    break
            if not encontrado:
                conteo.append((destino,1))
            
        # cant de pagos segun los medios de pago en ese periodo
        
            

