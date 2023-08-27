class Venda:
    identificador = 0
    def __init__(self, venda):
        Venda.identificador += 1
        self.identificador = Venda.identificador
        self.venda = venda
    def __str__(self):
        return f"identificador da venda: {self.identificador}   {self.venda}"
