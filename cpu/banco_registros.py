class BancoDeRegistros:
    def __init__(self, num_registros=9):
        """Inicializa el banco con una cantidad de registros especificada."""
        self.registros = [0] * num_registros

    def leer_registro(self, n):
        """Devuelve el valor almacenado en el registro especificado."""
        if 0 <= n < len(self.registros):
            return self.registros[n]
        else:
            raise IndexError("El número del registro está fuera de rango.")

    def escribir_registro(self, n, valor):
        """Escribe un valor en el registro especificado."""
        if 0 <= n < len(self.registros):
            self.registros[n] = valor
        else:
            raise IndexError("El número del registro está fuera de rango.")

    def mostrar_registros(self):
        """Devuelve una representación textual de todos los registros."""
        return " | ".join(f"R{idx}: {val}" for idx, val in enumerate(self.registros))

