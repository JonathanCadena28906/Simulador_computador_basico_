from memoria.memoria import Memoria
from memoria.permanente import MemoriaPermanente
from memoria.programa import MemoriaPrograma


class ControlMemoria:
    def __init__(self, tamaño_memoria, contenido_permanente, tamaño_programa):
        self.memoria_general = Memoria(tamaño_memoria)
        self.memoria_permanente = MemoriaPermanente(contenido_permanente)
        self.memoria_programa = MemoriaPrograma(tamaño_programa)

    def leer_memoria(self, tipo, direccion):
        """Lee un dato desde la memoria especificada."""
        if tipo == "general":
            return self.memoria_general.leer(direccion)
        elif tipo == "permanente":
            return self.memoria_permanente.leer(direccion)
        elif tipo == "programa":
            return self.memoria_programa.leer(direccion)
        else:
            raise ValueError("Tipo de memoria inválido.")

    def escribir_memoria(self, tipo, direccion, valor):
        """Escribe un dato en la memoria especificada."""
        if tipo == "general":
            self.memoria_general.escribir(direccion, valor)
        elif tipo == "programa":
            self.memoria_programa.escribir(direccion, valor)
        else:
            raise ValueError("No se puede escribir en la memoria especificada.")

