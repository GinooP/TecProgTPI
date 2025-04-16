from asiento import Asiento

class Unidad:
    # Una unidad tiene muchos asientos y una patente(identificador)
    def __init__(self, patente: str):
        self._patente = patente
        self._asientos = list[Asiento]