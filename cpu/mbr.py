 
class MBR:
    def __init__(self):
        self.dato = None

    def cargar(self, dato):
        """
        Carga un dato en el MBR.
        """
        self.dato = dato

    def leer(self):
        """
        Devuelve el dato almacenado.
        """
        return self.dato

    def limpiar(self):
        """
        Limpia el registro MBR.
        """
        self.dato = None
