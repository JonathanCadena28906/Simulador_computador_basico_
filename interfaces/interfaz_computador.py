import customtkinter as ctk
from interfaces.interfaz_io import InterfazIO
from interfaces.interfaz_cpu import Interfaz_CPU
from interfaces.interfaz_bus import InterfazBus
from interfaces.interfaz_memoria import InterfazMemoria


class InterfazComputador:
    def __init__(self, parent):
        # Crear el marco principal
        self.frame = ctk.CTkFrame(parent, width=1280, height=800)
        self.frame.pack(fill="both", expand=True)

        # Configurar las proporciones
        self.frame.columnconfigure(0, weight=3)  # 30% del ancho para I/O
        self.frame.columnconfigure(1, weight=4)  # 35% del ancho para CPU y espacio de buses (30% más pequeño)
        self.frame.columnconfigure(2, weight=4)  # 35% del ancho para Memorias (toma el espacio restante)
        self.frame.rowconfigure(0, weight=1)

        # Interfaz Entrada/Salida
        self.io_frame = ctk.CTkFrame(self.frame)
        self.io_frame.pack(side="left", fill="y", padx=10, pady=10)
        self.io = InterfazIO(self.io_frame)

        # Frame combinado para CPU y espacio de buses
        self.cpu_buses_frame = ctk.CTkFrame(self.frame)
        self.cpu_buses_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        # Altura fija de la CPU
        self.cpu_height = 400

        # Dibujar los buses directamente sobre el frame de la CPU
        self.buses = InterfazBus(self.cpu_buses_frame, cpu_height=self.cpu_height)

        # Interfaz CPU
        self.cpu = Interfaz_CPU(self.cpu_buses_frame, height=self.cpu_height)

        # Interfaz Memoria
        self.memoria_frame = ctk.CTkFrame(self.frame)
        self.memoria_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)
        self.memoria = InterfazMemoria(self.memoria_frame)

    def dibujar(self):
        # Simular dibujo actualizando los textos de las etiquetas
        self.io.execute_output()  # Simular acción en el IO
        self.cpu.dibujar()  # Llamar al método dibujar de la CPU
