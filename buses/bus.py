from abc import ABC, abstractmethod

class Bus(ABC):
    def __init__(self):
        self.datos = [] 

    @abstractmethod
    def enviar_datos(self, dato):
        pass

    @abstractmethod
    def recibir_datos(self):
        pass

