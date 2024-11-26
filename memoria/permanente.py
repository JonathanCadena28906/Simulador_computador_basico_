from memoria.memoria import Memoria


class MemoriaPermanente(Memoria):
    def __init__(self, contenido_inicial):
        super().__init__(len(contenido_inicial))
        self.datos = contenido_inicial[:]  # Copia el contenido inicial.

    def escribir(self, direccion, valor):
        """Sobrescribe el método para deshabilitar escritura."""
        raise ValueError("La memoria permanente es de solo lectura.")

