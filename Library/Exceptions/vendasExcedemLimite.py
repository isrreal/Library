class VendasExcedemLimite(Exception):
    def __init__(self, message):
        super().__init__(message)
        messagebox.showerror("Vendas Excedem Limite", message)
