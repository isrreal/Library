class LivroDeAventura(Livro):
    def __init__(self, titulo, quantidade):
        super().__init__(titulo, random.randrange(20, 70), quantidade, tipo = "Aventura")

