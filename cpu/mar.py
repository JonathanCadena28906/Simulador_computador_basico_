class MAR:
    def __init__(self):
        self.direccion = None

    def cargar(self, direccion):
        """
        Carga una dirección en el MAR.
        """
        self.direccion = direccion

    def leer(self):
        """
        Devuelve la dirección almacenada.
        """
        return self.direccion

    def limpiar(self):
        """
        Limpia el registro MAR.
        """
        self.direccion = None

