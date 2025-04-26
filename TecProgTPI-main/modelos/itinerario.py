from ciudad import Ciudad

class Itinerario:
    # Un itinerario tiene ciudades de inicio, fin e intermedias
    def __init__(self, ciudades:list[Ciudad]): #ciudad_origen, ciudad_destino, ciudades_de_paradas
        self._ciudades = ciudades