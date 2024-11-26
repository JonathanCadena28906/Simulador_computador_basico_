import customtkinter as ctk
from tkinter import filedialog
import os

class InterfazIO:

    def __init__(self, parent):
        # Crear el marco principal para la interfaz
        self.frame = ctk.CTkFrame(parent, width=0.2*1280, height=800)  # 20% del ancho de la pantalla
        self.frame.pack(side="left", fill="y", padx=10, pady=10)

        # Campo de entrada (INPUT)
        self.input_text = ctk.CTkTextbox(self.frame, wrap="word", width=0.9*1280*0.2, height=320)
        self.input_text.place(relx=0.05, rely=0.05)

        # Botones
        self.execute_button = ctk.CTkButton(self.frame, text="Ejecutar", width=0.9*1280*0.2, height=40, command=self.execute_output)
        self.execute_button.place(relx=0.05, rely=0.5)

        self.load_button = ctk.CTkButton(self.frame, text="Cargar", width=0.9*1280*0.2, height=40, command=self.load_file)
        self.load_button.place(relx=0.05, rely=0.58)

        self.save_button = ctk.CTkButton(self.frame, text="Guardar", width=0.9*1280*0.2, height=40, command=self.save_file)
        self.save_button.place(relx=0.05, rely=0.66)

        # Campo de salida (OUTPUT)
        self.output_text = ctk.CTkTextbox(self.frame, state="disabled", wrap="word", width=0.9*1280*0.2, height=160)
        self.output_text.place(relx=0.05, rely=0.75)

    def execute_output(self):
        """Copia el contenido de INPUT al OUTPUT."""
        input_content = self.input_text.get("1.0", "end-1c")  # Obtener texto de INPUT
        self.output_text.configure(state="normal")  # Habilitar edición
        self.output_text.delete("1.0", "end")  # Limpiar OUTPUT
        self.output_text.insert("1.0", input_content)  # Insertar texto en OUTPUT
        self.output_text.configure(state="disabled")  # Deshabilitar edición

    def load_file(self):
        """Carga un archivo .jjj de ../ejemplos_programas en el campo INPUT."""
        file_path = filedialog.askopenfilename(
            initialdir="../ejemplos_programas",
            title="Seleccionar archivo .jjj",
            filetypes=(("Archivos .jjj", "*.jjj"), ("Todos los archivos", "*.*"))
        )
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.input_text.delete("1.0", "end")  # Limpiar INPUT
                self.input_text.insert("1.0", content)  # Cargar contenido en INPUT

    def save_file(self):
        """Guarda el contenido de INPUT en un archivo .jjj en ../ejemplos_programas."""
        folder_path = "../ejemplos_programas"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        file_path = filedialog.asksaveasfilename(
            initialdir=folder_path,
            title="Guardar archivo como",
            defaultextension=".jjj",
            filetypes=(("Archivos .jjj", "*.jjj"),)
        )
        if file_path:
            input_content = self.input_text.get("1.0", "end-1c")
            with open(file_path, "w") as file:
                file.write(input_content)