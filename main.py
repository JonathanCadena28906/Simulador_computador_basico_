import customtkinter as ctk
from interfaces.interfaz_computador import InterfazComputador

def main():
    # Configuración de la ventana principal
    root = ctk.CTk()
    root.title("Simulador de Procesador")
    root.geometry("1280x800")

    # Crear la interfaz principal
    interfaz_computador = InterfazComputador(root)

    # Función para actualizar los componentes de forma periódica
    def actualizar():
        interfaz_computador.actualizar_componentes()
        root.after(1000, actualizar)

    # Iniciar actualización periódica


    # Inicia el bucle principal de la interfaz
    root.mainloop()

if __name__ == "__main__":
    main()
