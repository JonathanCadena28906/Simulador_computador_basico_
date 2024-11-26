class Pc:
    def __init__(self):
        self.valor = 0  # Inicializa el contador de programa a 0.

    def cargar_valor(self, valor):
        """Carga un valor específico en el PC."""
        if valor >= 0:
            self.valor = valor
        else:
            raise ValueError("El valor del PC no puede ser negativo.")

    def obtener_valor(self):
        """Devuelve el valor actual del PC."""
        return self.valor

    def incrementar(self):
        """Incrementa el valor del PC en 1."""
        self.valor += 1
