from medioPago import IMedioPago

class Uala(IMedioPago):
    # Este metodo de pago tiene un email y el nombre del titular
    def __init__(self, email:str, nombre_titular:str):
        super().__init__()
        self._email = email
        self._nombre_titular = nombre_titular