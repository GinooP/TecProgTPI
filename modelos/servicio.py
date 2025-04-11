from unidad import Unidad
from datetime import datetime

class Servicio:
    def __init__(
            self,
            unidad:Unidad,
            fecha_partida:datetime,
            fecha_llegada:datetime,
            calidad:str,
            precio:float
            ):
        self._unidad = unidad
        self._fecha_partida = fecha_partida
        self._fecha_llegada = fecha_llegada
        self._calidad = calidad
        self._precio = precio