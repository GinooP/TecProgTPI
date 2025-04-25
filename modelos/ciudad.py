class Ciudad:
    # Una ciudad tiene un codigo(identificador), nombre y provincia
    def __init__(self, codigo:str, nombre:str, provincia:str):
        self._codigo = codigo
        self._nombre = nombre
        self._provincia = provincia

    def getNombreCiudad(self):
        return self._nombre
