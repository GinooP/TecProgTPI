from pasajero import Pasajero

from datetime import datetime

class Reserva:
    # Una reserva tiene un pasajero y un asiento. Ademas posee la fecha y hora de la reserva
    def __init__(self, pasajero:Pasajero, fecha_y_hora:datetime):
        self._pasajero = pasajero
        self._fecha_y_hora = fecha_y_hora

    def getPasajero(self):
        return f"Pasajero {self._pasajero.getNombre()}, asiento {self._pasajero.getAsiento()}."
    