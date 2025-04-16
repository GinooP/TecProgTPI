from medioPago import IMedioPago

class MercadoPago(IMedioPago):
    # Este metodo de pago tiene un nro de celular y el email
    def __init__(self, celular:str, email:str):
        super().__init__() 
        self._celular = celular
        self._email = email