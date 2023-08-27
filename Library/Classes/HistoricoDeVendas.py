class HistoricoDeVendas:
    def __init__(self):
        self.__historico = []
    @property
    def historico(self):
        return self.__historico
    def push(self, venda):
        self.__historico.append(venda) 
