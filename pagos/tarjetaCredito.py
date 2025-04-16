from medioPago import IMedioPago
from datetime import date

class TarjetaCredito(IMedioPago):
    # Este metodo de pago tiene un nro de celular, el dni del titular, nombre de la tarjeta y fecha de vencimiento
    def __init__(self, numero:str, dni_titular:int, nombre:str, fecha_vencimiento:date):
        super().__init__()
        self._numero = numero
        self._dni_titular = dni_titular
        self._nombre = nombre
        self._fecha_vencimiento = fecha_vencimiento