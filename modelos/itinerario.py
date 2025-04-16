from ciudad import Ciudad

class Itinerario:
    # Un itinerario tiene ciudades de inicio, fin e intermedias
    def __init__(self, ciudad_origen:Ciudad, ciudad_destino:Ciudad, ciudades_de_paradas:list[Ciudad]):
        self._ciudade_de_origen = ciudad_origen
        self._ciudade_de_destino = ciudad_destino
        self._ciudades_de_parada = ciudades_de_paradas

    