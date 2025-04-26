from ciudad import Ciudad

class Itinerario:
    # Un itinerario tiene ciudades de inicio, fin e intermedias
    def __init__(self, ciudad_origen:Ciudad, ciudad_destino:Ciudad, ciudades_de_paradas:list[Ciudad]):
        self._ciudad_de_origen = ciudad_origen
        self._ciudad_de_destino = ciudad_destino
        self._ciudades_de_parada = ciudades_de_paradas

    #Retorna un string con todas los nombres de las ciudades del itinerario listadas.
    def mostrarItinerario (self):
        stringFinal=[]
        stringFinal.append(f"Ciudad de origen: {self._ciudad_de_origen.getNombreCiudad()}")
        stringFinal.append(f"Ciudad de destino: {self._ciudad_de_destino.getNombreCiudad()}")
        cantParadas=0
        for ciudad in self._ciudades_de_parada:
            cantParadas=cantParadas+1
            stringFinal.append(f"Parada Nro. {cantParadas} : {ciudad.getNombreCiudad()}")
        return "\n".join(stringFinal)