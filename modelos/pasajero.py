from asiento import Asiento

class Pasajero:

    # Un pasajero tiene nombre, email y dni(identificador)
    def __init__(self, nombre:str, email:str, dni:int, asiento:Asiento):
        self._nombre = nombre
        self._email = email
        self._dni = dni
        self._asiento = asiento

    def getNombre(self):
        return self._nombre
    def getAsiento(self):
        return self._asiento