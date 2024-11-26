import customtkinter as ctk
import tkinter as tk

class InterfazMemoria:
    def __init__(self, parent):
        # Crear el marco principal para la interfaz de memoria
        self.frame = ctk.CTkFrame(parent)
        self.frame.pack(fill="both", expand=True)

        # Crear etiquetas para las matrices
        self.label1 = ctk.CTkLabel(self.frame, text="Memoria Datos", font=("Arial", 16))
        self.label1.pack(side="top", pady=(5, 0))

        self.canvas1 = tk.Canvas(self.frame, bg="lightgray")
        self.canvas1.pack(side="top", fill="both", expand=True, padx=5, pady=5)

        self.label2 = ctk.CTkLabel(self.frame, text="Memoria Programa", font=("Arial", 16))
        self.label2.pack(side="top", pady=(5, 0))

        self.canvas2 = tk.Canvas(self.frame, bg="lightgray")
        self.canvas2.pack(side="top", fill="both", expand=True, padx=5, pady=5)

        # Inicializar las matrices para los canvas
        self.matriz1 = []
        self.matriz2 = []

        # Crear matrices dinámicas
        self.crear_matriz_dinamica(self.canvas1, self.matriz1, 1)
        self.crear_matriz_dinamica(self.canvas2, self.matriz2, 2)

    def crear_matriz_dinamica(self, canvas, matriz, canvas_index):
        """
        Crea una matriz dentro de un canvas y numera las celdas de la primera columna en orden ascendente.
        """
        def ajustar_matriz(event):
            canvas.delete("all")  # Limpiar el canvas
            matriz.clear()  # Limpiar la matriz

            # Calcular dimensiones dinámicas
            canvas_width = canvas.winfo_width()
            canvas_height = canvas.winfo_height()
            cols = 2  # Siempre dos columnas

            # Ajustar las proporciones de las columnas
            col_widths = [canvas_width // 4, (canvas_width * 3) // 4]  # 1/4 y 3/4
            cell_height = canvas_height // 20  # Dividir en 20 filas

            for row in range(20):
                row_cells = []
                for col in range(cols):
                    if col == 0:
                        x1 = 0
                        x2 = col_widths[0]
                    else:
                        x1 = col_widths[0]
                        x2 = canvas_width

                    y1 = row * cell_height
                    y2 = y1 + cell_height

                    # Crear una celda
                    cell = canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="black")
                    
                    # Número ascendente en la primera columna
                    text_value = str(row + 1) if col == 0 else ""  # Cambiar a ascendente
                    text = canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=text_value, fill="black")
                    
                    row_cells.append((cell, text))
                matriz.append(row_cells)

        # Vincular el evento de cambio de tamaño
        canvas.bind("<Configure>", ajustar_matriz)


    def actualizar_celda(self, canvas_index, row, col, texto):
        """
        Actualiza el texto de una celda en una matriz específica.
        
        :param canvas_index: Índice del canvas (1 para matriz1, 2 para matriz2).
        :param row: Fila de la celda a actualizar.
        :param col: Columna de la celda a actualizar.
        :param texto: Nuevo texto para la celda.
        """
        matriz = self.matriz1 if canvas_index == 1 else self.matriz2
        if 0 <= row < len(matriz) and 0 <= col < len(matriz[row]):
            _, text_id = matriz[row][col]
            canvas = self.canvas1 if canvas_index == 1 else self.canvas2
            canvas.itemconfig(text_id, text=texto)

# Ejemplo de uso:
if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry("600x600")
    interfaz = InterfazMemoria(root)
    
    # Actualizar celdas después de la creación
    root.after(1000, lambda: interfaz.actualizar_celda(1, 5, 1, "Dato"))
    root.after(2000, lambda: interfaz.actualizar_celda(2, 10, 1, "Instrucción"))

    root.mainloop()
