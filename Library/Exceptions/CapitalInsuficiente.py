
class CapitalInsuficiente(Exception):
    def __init__(self, message):
        super().__init__(message)
        messagebox.showerror("Capital Insuficiente", message)
