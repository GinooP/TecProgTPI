from modelos.pasajero import Pasajero

class Asiento:
    # Un asiento tiene un numero(identificador) y un estado(está ocupado o no)
    def __init__(self, numero:int, ocupado:bool):
       self._ocupado = ocupado
 
    def verAsiento(self):
        if not self._ocupado:
            return f" {self._numero},"
        else:
            return None
        
    def reservar(self, pasajero:Pasajero):
        pass
