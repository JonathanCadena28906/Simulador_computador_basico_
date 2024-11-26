class IR:
    def __init__(self):
        self.instruccion = None

    def cargar(self, instruccion):
        """
        Carga una nueva instrucción en el IR.
        """
        self.instruccion = instruccion

    def leer(self):
        """
        Devuelve la instrucción almacenada.
        """
        return self.instruccion

    def limpiar(self):
        """
        Limpia el registro de instrucción.
        """
        self.instruccion = None

