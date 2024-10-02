from tkinter import simpledialog
from tkinter import messagebox
from tkinter import Button
from tkinter import Label 
from tkinter import Frame 
from tkinter import StringVar
from tkinter import Listbox
from tkinter import OptionMenu
from tkinter import *

class CapitalInsuficiente(Exception):
    def __init__(self, message):
        super().__init__(message)
        messagebox.showerror("Capital Insuficiente", message)

class LivroInexistente(Exception):
    def __init__(self, message):
        super().__init__(message)
        messagebox.showerror("Livro Inexistente", message)

class VendasExcedemLimite(Exception):
    def __init__(self, message):
        super().__init__(message)
        messagebox.showerror("Vendas Excedem Limite", message)
