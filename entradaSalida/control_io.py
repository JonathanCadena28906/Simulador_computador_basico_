from entradaSalida import entrada
from entradaSalida import salida


class ControlIO:
    def __init__(self):
        self.entrada = entrada()
        self.salida = salida()

    def leer_entrada(self):
        """Lee datos desde el dispositivo de entrada."""
        pass

    def escribir_salida(self, dato):
        """Escribe datos al dispositivo de salida."""
        pass

