class Decodificador:
    def __init__(self, memoria, registros, alu, control_bus):
        """
        Inicializa el decodificador con referencias a los componentes principales.
        """
        self.memoria = memoria
        self.registros = registros
        self.alu = alu
        self.control_bus = control_bus

        self.opcodes = {
            "0000": "LOAD",
            "0001": "STORE",
            "0010": "MOVE",
            "0011": "ADD",
            "0100": "SUB",
            "0101": "MUL",
            "0110": "DIV",
            "0111": "MOD",
            "1000": "AND",
            "1001": "OR",
            "1010": "XOR",
            "1011": "NOT",
            "1100": "READ",
            "1101": "WRITE",
            "1110": "JMP",
            "1111": "CMP"
        }