from datetime import datetime
from asiento import Asiento
from pasajero import Pasajero
from pagos.medioPago import MedioPago

class Venta:
    # Una venta tiene un asiento, un medio de pago y un pasajero asociado.
    # Ademas posee la fecha y hora de la transaccion
    def __init__(self, fecha_y_hora:datetime, asiento:Asiento, medio_de_pago:MedioPago, pasajero:Pasajero):
        self._fecha_y_hora = fecha_y_hora
        self._asiento = asiento
        self._medio_de_pago = medio_de_pago
        self._pasajero = pasajero