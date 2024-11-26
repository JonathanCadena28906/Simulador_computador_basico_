class CompiladorRISC:
    def __init__(self):
        self.opcodes = {
            "LOAD": "0000",
            "STORE": "0001",
            "MOVE": "0010",
            "ADD": "0011",
            "SUB": "0100",
            "MUL": "0101",
            "DIV": "0110",
            "MOD": "0111",
            "AND": "1000",
            "OR": "1001",
            "XOR": "1010",
            "NOT": "1011",
            "READ": "1100",
            "WRITE": "1101",
            "JMP": "1110",
            "CMP": "1111"
        }

        self.modos_direccionamiento = {
            "INMEDIATO": "000",
            "DIRECTO": "001",
            "INDIRECTO": "010",
            "POR_REGISTRO": "011",
            "POR_REGISTRO_DIRECTO": "100"
        }

    def ensamblar(self, linea):
        """
        Convierte una línea de ensamblador a código máquina.
        """
        partes = linea.strip().split()
        if len(partes) < 2:
            raise ValueError(f"Línea inválida: {linea}")
        
        instruccion = partes[0].upper()
        if instruccion not in self.opcodes:
            raise ValueError(f"Instrucción no reconocida: {instruccion}")

        opcode = self.opcodes[instruccion]
        operandos = partes[1:]
        oper1, oper2, modo1, modo2 = "00000000", "00000000", "000", "000"

        if instruccion in {"LOAD", "STORE", "MOVE", "ADD", "SUB", "MUL", "DIV", "MOD", "AND", "OR", "XOR", "CMP"}:
            oper1, modo1 = self._procesar_operando(operandos[0])
            if len(operandos) > 1:
                oper2, modo2 = self._procesar_operando(operandos[1])

        elif instruccion in {"NOT", "READ", "WRITE"}:
            oper1, modo1 = self._procesar_operando(operandos[0])

        elif instruccion == "JMP":
            oper1, modo1 = self._procesar_operando(operandos[0])

        else:
            raise ValueError(f"Instrucción no soportada: {instruccion}")

        # Ensamblar la instrucción completa
        instruccion_maquina = f"{opcode}{oper1}{oper2}{modo1}{modo2}"
        return instruccion_maquina

    def _procesar_operando(self, operando):
        """
        Procesa un operando y retorna su representación binaria y modo de direccionamiento.
        """
        if operando.startswith("[[") and operando.endswith("]]"):
            # Modo indirecto
            direccion = operando[2:-2]
            return self._to_bin(direccion, 8), self.modos_direccionamiento["INDIRECTO"]
        elif operando.startswith("[") and operando.endswith("]"):
            # Modo directo
            direccion = operando[1:-1]
            return self._to_bin(direccion, 8), self.modos_direccionamiento["DIRECTO"]
        elif operando.startswith("R"):
            # Modo por registro
            registro = operando[1:]
            return self._to_bin(registro, 8), self.modos_direccionamiento["POR_REGISTRO"]
        elif operando.isdigit():
            # Modo inmediato
            return self._to_bin(operando, 8), self.modos_direccionamiento["INMEDIATO"]
        else:
            raise ValueError(f"Operando no reconocido: {operando}")

    @staticmethod
    def _to_bin(valor, bits):
        """
        Convierte un valor decimal a binario con una longitud fija.
        """
        binario = bin(int(valor))[2:]
        if len(binario) > bits:
            raise ValueError(f"Valor fuera de rango: {valor} para {bits} bits")
        return binario.zfill(bits)

    def compilar(self, codigo):
        """
        Compila un conjunto de instrucciones en ensamblador a código máquina.
        """
        instrucciones_maquina = []
        for linea in codigo.splitlines():
            if linea.strip() and not linea.strip().startswith(";"):  # Ignorar líneas vacías y comentarios
                try:
                    instruccion_maquina = self.ensamblar(linea)
                    instrucciones_maquina.append(instruccion_maquina)
                except ValueError as e:
                    print(f"Error al compilar la línea '{linea}': {e}")
        return instrucciones_maquina

