from buses import bus_control, bus_datos, bus_direccion


class ControlBus:
    def __init__(self):
        self.bus_datos = bus_datos()  # Instancia del BusDatos
        self.bus_control = bus_control()  # Instancia del BusControl
        self.bus_direccion = bus_direccion()  # Instancia del BusDireccion

    def iniciar_transferencia(self, dato, direccion, senal):
       pass

    def finalizar_transferencia(self):
       pass

    def estado_bus(self):
        pass

