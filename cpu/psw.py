class PSW:
    def __init__(self):
        self.flags = {"zero": 0, "negative": 0, "overflow": 0, "carry": 0}

    def actualizar(self, flag, valor):
        """
        Actualiza un flag específico.
        """
        if flag in self.flags:
            self.flags[flag] = valor
        else:
            raise ValueError(f"Flag no reconocido: {flag}")

    def leer(self, flag):
        """
        Devuelve el valor de un flag específico.
        """
        if flag in self.flags:
            return self.flags[flag]
        else:
            raise ValueError(f"Flag no reconocido: {flag}")

    def reiniciar(self):
        """
        Reinicia todos los flags.
        """
        for flag in self.flags:
            self.flags[flag] = 0

