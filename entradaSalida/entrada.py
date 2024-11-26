class Entrada:
    def __init__(self):
        self.buffer = []  # Buffer de datos entrantes.

    def agregar_dato(self, dato):
        """Agrega un dato al buffer de entrada."""
        self.buffer.append(dato)

    def leer(self):
        """Lee el siguiente dato del buffer de entrada."""
        if self.buffer:
            return self.buffer.pop(0)
        else:
            raise ValueError("No hay datos disponibles en la entrada.")

