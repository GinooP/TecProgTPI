from sistema.argentur import Argentur
from modelos.venta import Venta
from modelos.servicio import Servicio
from modelos.unidad import Unidad
from modelos.asiento import Asiento
from modelos.itinerario import Itinerario
from modelos.ciudad import Ciudad
from modelos.pasajero import Pasajero
from datetime import date

def main():
    sistema = Argentur(True,[],[])
    asientos = [Asiento(1,False),
                Asiento(2,False),
                Asiento(3,False),
                Asiento(4,False),
                Asiento(5,False)]
    unidad1 = Unidad("AB 123 CD",asientos)
    fecha_salida1 = date(2025,11,22)
    fecha_llegada1 = date(2025,12,22)
    ciudad_origen1 = Ciudad("3000","Santa Fe", "Santa Fe")
    ciudad_destino1 = Ciudad("3050","Calchaqui", "Santa Fe")
    ciudades_de_parada1 = [Ciudad("3001","Rosario", "Santa Fe"),
                            Ciudad("3002","Ceres", "Santa Fe"),
                            Ciudad("3003","San Javier", "Santa Fe"),
                            Ciudad("3004","Reconquista", "Santa Fe"),
                            Ciudad("3005","Las Toscas", "Santa Fe"),
                            Ciudad("3006","Avellaneda", "Santa Fe"),
                            Ciudad("3007","Villa Ocampo", "Santa Fe"),
                            Ciudad("3008","Las Parejas", "Santa Fe"),
                            Ciudad("3009","San Justo", "Santa Fe"),
                            Ciudad("3010","Esperanza", "Santa Fe")]

    itinerario1 = Itinerario(ciudad_origen1,ciudad_destino1,ciudades_de_parada1)
    servicio1 = Servicio(100,unidad1,fecha_salida1,fecha_llegada1,"Comun",1999.99,itinerario1,[],[])
    sistema.agregarServicio(servicio1)
    print(sistema.consultarServicios())
    sistema.simularReserva(date.today()) 

if __name__ == "__main__":
    main()