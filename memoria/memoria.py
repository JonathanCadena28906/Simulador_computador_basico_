class Memoria:
    def __init__(self, tamaño):
        self.datos = [0] * tamaño  # Inicializa la memoria con ceros.

    def leer(self, direccion):
        """Lee un dato desde una dirección específica."""
        if 0 <= direccion < len(self.datos):
            return self.datos[direccion]
        else:
            raise ValueError(f"Dirección inválida: {direccion}")

    def escribir(self, direccion, valor):
        """Escribe un dato en una dirección específica."""
        if 0 <= direccion < len(self.datos):
            self.datos[direccion] = valor
        else:
            raise ValueError(f"Dirección inválida: {direccion}")

    def mostrar_contenido(self):
        """Devuelve el contenido completo de la memoria."""
        return self.datos

