class Pasajero:
    # Un pasajero tiene nombre, email y dni(identificador)
    def __init__(self, nombre:str, email:str, dni:int):
        self._nombre = nombre
        self._email = email
        self._dni = dni