import customtkinter as ctk
import tkinter as tk


class InterfazBus:
    def __init__(self, parent, cpu_height):
        # Canvas incrustado dentro del frame proporcionado
        self.canvas = tk.Canvas(parent, bg="gray", highlightthickness=0)
        self.canvas.place(relx=0, rely=0, relwidth=1, relheight=1)  # Ocupa todo el espacio del frame

        self.color_datos = "blue"
        self.color_direcciones = "green"
        self.color_control = "red"
        self.font = ("Arial", 10, "bold")
        self.buses = {}
        self.cpu_height = cpu_height  # Altura de la CPU

        # Asegurar que el dibujo se haga después de que el Canvas esté renderizado
        self.canvas.bind("<Configure>", self.on_configure)

    def on_configure(self, event=None):
        """Se ejecuta cuando el Canvas cambia de tamaño."""
        # Validar que el canvas tenga dimensiones válidas
        if self.canvas.winfo_width() > 0 and self.canvas.winfo_height() > 0:
            self.inicializar_buses()
            self.dibujar()

    def inicializar_buses(self):
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        # Definir los límites de la región rosada
        pink_start_x = canvas_width * 0.7  # Ajustar el inicio horizontal de la región rosada
        pink_end_x = canvas_width * 0.9    # Ajustar el final horizontal de la región rosada
        pink_start_y = self.cpu_height * 0.05  # Comienza casi al tope del área rosada
        pink_end_y = canvas_height * 0.95   # Límite inferior del área rosada

        # Coordenadas base de los buses dentro de la región rosada
        base_x = (pink_start_x + pink_end_x) / 2
        separation = (pink_end_x - pink_start_x) / 2  # Aumentar la separación entre buses
        bus_width = separation / 6  # Ajustar el ancho proporcionalmente

        # Calcular posiciones escaladas para los buses
        self.buses = {
            "datos": {
                "color": self.color_datos,
                "start": (base_x - separation, pink_start_y),
                "end": (base_x - separation, pink_end_y * 0.85),
                "label": "Bus de Datos",
                "width": bus_width,
                "estado": "Activo",
            },
            "direcciones": {
                "label": "Bus de Direcciones",
                "color": self.color_direcciones,
                "start": (base_x, pink_start_y + (pink_end_y * 0.1)),  # Escalado hacia abajo
                "end": (base_x, pink_end_y * 0.92),
                "width": bus_width,
                "estado": "Inactivo",
            },
            "control": {
                "color": self.color_control,
                "start": (base_x + separation, pink_start_y + (pink_end_y * 0.15)),  # Escalado hacia abajo
                "end": (base_x + separation, pink_end_y),
                "label": "Bus de Control",
                "width": bus_width,
                "estado": "Activo",
            },
        }

    def dibujar(self):
        # Limpiar el canvas antes de dibujar
        self.canvas.delete("all")
        
        # Diccionario para almacenar los IDs de las líneas por bus
        self.line_ids = {}
        
        # Dibujar los buses
        for bus_name, bus_data in self.buses.items():
            color = bus_data["color"]
            start = bus_data["start"]
            end = bus_data["end"]
            width = bus_data["width"]
            
            # Almacenar el ID de la línea en el diccionario
            self.line_ids[bus_name] = {
                "Bus_principal": self.canvas.create_line(start[0], start[1], end[0], end[1], fill=color, width=int(width)),
                "label": self.draw_vertical_label(bus_data["label"], start[0] - 30, start[1], color),
                "Conexion_memoria_datos": self.crear_conexion_memoria_datos(start, end, color, width),
                "Conexion_memoria_programa": self.crear_conexion_memoria_programa(start, end, color, width),
                "Conexion_i_o": self.crear_conexion_i_o(start, end, color, width),
            }

    """
    line_datos = self.line_ids["datos"]

    # Ejemplo: acceder a elementos específicos
    line_id = line_datos["line"]         # ID de la línea principal
    label_id = line_datos["label"]       # ID de la etiqueta
    estado_id = line_datos["estado"]     # ID del estado visual
    connections = line_datos["connections"]  # IDs de las conexiones horizontales

    print(f"ID de la línea: {line_id}, Etiqueta: {label_id}, Estado: {estado_id}")


    """


    def draw_vertical_label(self, text, x, y, color):
        """Dibuja la etiqueta vertical para un bus."""
        if text:
            for i, char in enumerate(text):
                self.canvas.create_text(x, y + i * 10, text=char, fill=color, font=self.font)

    def draw_bus_status(self, estado, x, y, color):
        """Dibuja el estado del bus."""
        if estado:
            self.canvas.create_text(x, y, text=f"Estado: {estado}", fill=color, font=("Arial", 12, "bold"))

    def crear_conexion_memoria_datos(self, start, end, color, width):
        """
        Crea la conexión horizontal superior (relacionada con memoria/datos).
        La línea comienza desde el final del bus y se extiende hacia el borde derecho del canvas.
        
        :param start: Coordenadas de inicio del bus (x, y).
        :param end: Coordenadas de fin del bus (x, y).
        :param color: Color de la línea.
        :param width: Grosor de la línea.
        :return: ID de la línea creada.
        """
        canvas_width = self.canvas.winfo_width()  # Obtener el ancho actual del canvas
        # Crear la línea y devolver su ID
        return self.canvas.create_line(end[0] - int(width / 2), start[1], canvas_width, start[1], fill=color, width=int(width))


    def crear_conexion_i_o(self, start, end, color, width):
        """
        Crea la conexión horizontal inferior (relacionada con I/O).
        La línea comienza desde el borde izquierdo del canvas y termina al inicio del bus.
        
        :param start: Coordenadas de inicio del bus (x, y).
        :param end: Coordenadas de fin del bus (x, y).
        :param color: Color de la línea.
        :param width: Grosor de la línea.
        :return: ID de la línea creada.
        """
        # Crear la línea y devolver su ID
        return self.canvas.create_line(0, end[1], start[0] + int(width / 2), end[1], fill=color, width=int(width))


    def crear_conexion_memoria_programa(self, start, end, color, width):
        """
        Crea la conexión horizontal para la memoria del programa.
        La línea comienza al final del bus y se extiende hasta el borde derecho del canvas.
        
        :param start: Coordenadas de inicio del bus (x, y).
        :param end: Coordenadas de fin del bus (x, y).
        :param color: Color de la línea.
        :param width: Grosor de la línea.
        :return: ID de la línea creada.
        """
        frame_width = self.canvas.winfo_width()  # Obtener el ancho actual del canvas
        # Crear la línea y devolver su ID
        return self.canvas.create_line(end[0], end[1], frame_width, end[1], fill=color, width=int(width))


    def actualizar_color_linea(self, bus_name, new_color):
        """
        Actualiza el color de todas las líneas asociadas a un bus.
        
        :param bus_name: El nombre del bus (clave en self.line_ids) cuyo color se desea cambiar.
        :param new_color: El nuevo color que se aplicará a las líneas asociadas al bus.
        """
        # Verificar si el bus existe en el diccionario line_ids
        if bus_name in self.line_ids:
            # Recorrer las claves dentro de self.line_ids[bus_name] (líneas asociadas al bus)
            for key, line_id in self.line_ids[bus_name].items():
                # Verificar si el valor es un ID válido (por ejemplo, una línea del canvas)
                if isinstance(line_id, int):  # Asegura que sea un ID de un elemento gráfico
                    # Actualizar el color de la línea en el canvas
                    self.canvas.itemconfig(line_id, fill=new_color)
            
            # Actualizar el color en el diccionario self.buses para mantener coherencia
            if bus_name in self.buses:
                self.buses[bus_name]["color"] = new_color
        else:
            print(f"El bus '{bus_name}' no existe o no tiene líneas asociadas.")
