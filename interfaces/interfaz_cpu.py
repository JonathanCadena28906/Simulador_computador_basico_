import customtkinter as ctk
import tkinter as tk


class Interfaz_CPU:
    def __init__(self, parent, height):
        # Crear el marco principal de la CPU
        self.frame = ctk.CTkFrame(parent, width=height, height=height, corner_radius=0)
        self.frame.pack(side="top", padx=10, pady=10, anchor="nw")  # Anclado arriba y a la izquierda

        # Dimensiones básicas
        self.side_length = height  # El lado de la CPU es igual a la altura disponible
        self.unit_width = self.side_length * 0.2  # Proporción para los rectángulos pequeños
        self.unit_height = self.side_length * 0.1

        # ALU - Triángulo invertido
        self.alu_canvas = tk.Canvas(self.frame, width=self.unit_width, height=self.unit_width, bg="white", highlightthickness=0)
        self.alu_canvas.place(relx=0.02, rely=0.05)  # Esquina superior izquierda ajustada
        self.alu_canvas.create_polygon(
            0, 0,
            self.unit_width, 0,
            self.unit_width // 2, self.unit_width,
            fill="yellow", outline="black"
        )
        alu_label = ctk.CTkLabel(self.frame, text="ALU", font=("Arial", 12))
        alu_label.place(relx=0.02, rely=0.01)

        # PSW - Rectángulo debajo de la ALU
        self.psw = ctk.CTkFrame(self.frame, width=self.unit_width, height=self.unit_height, fg_color="white", corner_radius=5)
        self.psw.place(relx=0.02, rely=0.3)
        psw_label = ctk.CTkLabel(self.frame, text="PSW", font=("Arial", 12))
        psw_label.place(relx=0.02, rely=0.26)

        # BRVS - Rectángulo debajo del PSW
        self.brvs = ctk.CTkFrame(self.frame, width=self.unit_width, height=self.unit_height, fg_color="white", corner_radius=5)
        self.brvs.place(relx=0.02, rely=0.5)
        brvs_label = ctk.CTkLabel(self.frame, text="BRVS", font=("Arial", 12))
        brvs_label.place(relx=0.02, rely=0.46)

        # IR - Rectángulo lado derecho
        self.ir = ctk.CTkFrame(self.frame, width=self.unit_width, height=self.unit_height, fg_color="white", corner_radius=5)
        self.ir.place(relx=0.35, rely=0.05)  # Ajuste horizontal hacia la izquierda
        ir_label = ctk.CTkLabel(self.frame, text="IR", font=("Arial", 12))
        ir_label.place(relx=0.35, rely=0.01)

        # UC - Cuadrado debajo del IR
        self.uc = ctk.CTkFrame(self.frame, width=self.unit_width, height=self.unit_width, fg_color="white", corner_radius=5)
        self.uc.place(relx=0.35, rely=0.3)
        uc_label = ctk.CTkLabel(self.frame, text="UC", font=("Arial", 12))
        uc_label.place(relx=0.35, rely=0.26)

        # MAR, MBR, PC - Rectángulos debajo de la UC
        self.mar = ctk.CTkFrame(self.frame, width=self.unit_width, height=self.unit_height, fg_color="white", corner_radius=5)
        self.mar.place(relx=0.35, rely=0.6)
        mar_label = ctk.CTkLabel(self.frame, text="MAR", font=("Arial", 12))
        mar_label.place(relx=0.35, rely=0.56)

        self.mbr = ctk.CTkFrame(self.frame, width=self.unit_width, height=self.unit_height, fg_color="white", corner_radius=5)
        self.mbr.place(relx=0.35, rely=0.75)
        mbr_label = ctk.CTkLabel(self.frame, text="MBR", font=("Arial", 12))
        mbr_label.place(relx=0.35, rely=0.71)

        self.pc = ctk.CTkFrame(self.frame, width=self.unit_width, height=self.unit_height, fg_color="white", corner_radius=5)
        self.pc.place(relx=0.35, rely=0.9)
        pc_label = ctk.CTkLabel(self.frame, text="PC", font=("Arial", 12))
        pc_label.place(relx=0.35, rely=0.86)
