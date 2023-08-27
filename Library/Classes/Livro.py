class Livro(object):
    def __init__(self, titulo, valor, quantidade, tipo):
        self.__identificador = ''.join(random.choices(string.digits, k = 10))
        self.__titulo = titulo
        self.__valor = valor
        self.__quantidade = quantidade
        self.__tipo = tipo
    @property
    def identificador(self):
        return self.__identificador
    @property
    def titulo(self):
        return self.__titulo
    @property
    def valor(self):
        return self.__valor
    @property
    def tipo(self):
        return self.__tipo
    @property
    def quantidade(self):
        return self.__quantidade
    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade += quantidade
    def __str__(self):
        return f"""-identificador: {self.identificador}     - título: {self.titulo}     - valor: R$ {self.valor}    - tipo: {self.tipo}     - quantidade: {self.quantidade}  """
    def __eq__(self, livro2):
        return True if self.identificador == livro2.identificador else False

