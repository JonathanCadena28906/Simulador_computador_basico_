class ALU:
    def __init__(self):
        self.flags = {"zero": 0, "negative": 0, "overflow": 0}

    def _actualizar_flags(self, resultado):
        self.flags["zero"] = int(resultado == 0)
        self.flags["negative"] = int(resultado < 0)
        # Aquí se podría calcular el flag de overflow si es relevante según la arquitectura.

    def sumar(self, operando1, operando2):
        resultado = operando1 + operando2
        self._actualizar_flags(resultado)
        return resultado

    def restar(self, operando1, operando2):
        resultado = operando1 - operando2
        self._actualizar_flags(resultado)
        return resultado

    def multiplicar(self, operando1, operando2):
        resultado = operando1 * operando2
        self._actualizar_flags(resultado)
        return resultado

    def dividir(self, operando1, operando2):
        if operando2 == 0:
            raise ZeroDivisionError("División por cero no permitida")
        resultado = operando1 // operando2
        self._actualizar_flags(resultado)
        return resultado

    def modulo(self, operando1, operando2):
        resultado = operando1 % operando2
        self._actualizar_flags(resultado)
        return resultado

    def and_logico(self, operando1, operando2):
        resultado = operando1 & operando2
        self._actualizar_flags(resultado)
        return resultado

    def or_logico(self, operando1, operando2):
        resultado = operando1 | operando2
        self._actualizar_flags(resultado)
        return resultado

    def xor_logico(self, operando1, operando2):
        resultado = operando1 ^ operando2
        self._actualizar_flags(resultado)
        return resultado

    def not_logico(self, operando):
        resultado = ~operando
        self._actualizar_flags(resultado)
        return resultado

    def comparar(self, operando1, operando2):
        self.flags["zero"] = int(operando1 == operando2)
        self.flags["negative"] = int(operando1 < operando2)

