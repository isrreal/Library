class LivroInexistente(Exception):
    def __init__(self, message):
        super().__init__(message)
        messagebox.showerror("Livro Inexistente", message)
