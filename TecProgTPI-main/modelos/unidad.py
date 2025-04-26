from asiento import Asiento

class Unidad:
    # Una unidad tiene muchos asientos y una patente(identificador)
    def __init__(self, patente: str, asientos:list[Asiento]):
        self._patente = patente
        self._asientos = asientos

    def listarAsientosDisponibles(self):
        asientosDisponibles = []
        for asiento in self._asientos:
            nroAsiento = asiento.verAsiento()
            if nroAsiento != None:
                asientosDisponibles.append(nroAsiento)
                
        return asientosDisponibles

    def ocuparAsiento(self,idAsiento):
        for asiento in self._asientos:
            if id(asiento)==idAsiento:
                asiento.ocupar()         