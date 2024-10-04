from tkinter import simpledialog
from tkinter import messagebox
from tkinter import Button
from tkinter import Label 
from tkinter import Frame 
from tkinter import StringVar
from tkinter import Listbox
from tkinter import OptionMenu
from tkinter import *
from functools import partial
import random
import re

from Classes import *
from Exceptions import *


def copiar_identificador(lista, window):
    window.clipboard_clear()
    valores = lista.curselection()
    if lista:
        id = re.findall("[0-9]+", lista.get(valores[0]))[0]
        window.clipboard_append(id)
        messagebox.showinfo("Copiar identificador", "Identificador copiado com sucesso!")

def switch_type(tipo, second_screen, livraria):
    second_screen.destroy()
    if tipo.get() == "Drama":
        titulo = simpledialog.askstring("Comprar livro", "Digite o título do livro")
        quantidade = simpledialog.askinteger("Comprar livro", "Digite a quantidade de livros")
        livraria.comprar_livro(LivroDeDrama(titulo, quantidade))
    elif tipo.get() == "Comédia":
        titulo = simpledialog.askstring("Comprar livro", "Digite o título do livro")
        quantidade = simpledialog.askinteger("Comprar livro", "Digite a quantidade de livros")
        livraria.comprar_livro(LivroDeComedia(titulo, quantidade))
    elif tipo.get() == "Aventura":
        titulo = simpledialog.askstring("Comprar livro", "Digite o título do livro")
        quantidade = simpledialog.askinteger("Comprar livro", "Digite a quantidade de livros")
        livraria.comprar_livro(LivroDeAventura(titulo, quantidade))

def comprar_livro(livraria: Livraria):
    second_screen = Tk()
    second_screen.maxsize(480, 360)
    second_screen.title("Selecionar tipo")
    moldura = Frame(second_screen)
    moldura.pack()
    valor = StringVar(moldura)
    option_types = ["Aventura", "Comédia", "Drama"] 
    valor.set("Escolha o tipo do livro")
    lista_de_opcoes = OptionMenu(moldura, valor, *option_types)
    lista_de_opcoes.pack()
    botao_confirma = Button(moldura, text = "Confirmar", command = partial(switch_type, valor, second_screen, livraria)).pack()

def vender_livro(livraria: Livraria):
    identificador_do_livro = simpledialog.askstring("Vender livro", "Digite o idenfificador do livro a se vender")
    quantidade = simpledialog.askinteger("Vender livro", "Digite a quantidade a se vender")
    book = list(filter(lambda x: x.identificador == identificador_do_livro, livraria.estoque))
    raise LivroInexistente("O livro a se vender não existe no estoque!") if not book else livraria.vender_livro(book[0], quantidade) 

def consultar_estoque(livraria: Livraria, window):
    if not livraria.estoque:
        messagebox.showinfo("Estoque", "Não há livros no estoque")
    else:
        second_screen = Tk()
        second_screen.title("Estoque")
        lista = Listbox(second_screen)
        for iterator in livraria.estoque:
            lista.insert(END, str(iterator))
        lista.pack(fill = BOTH, expand = True)
        botao_copiar_identificador = Button(second_screen, text = "Copiar Identificador", command = partial(copiar_identificador, lista, window)).pack()

def consultar_montante(livraria: Livraria):
    messagebox.showinfo("Montante", f"R$ {livraria.montante}")

def consultar_historico_de_vendas(livraria: Livraria): 
    if not livraria.historico_de_vendas:
        messagebox.showinfo("Histórico de vendas", "Ainda não há vendas!")
    else:
        second_screen = Tk()
        second_screen.title("Histórico de Vendas")
        historico_de_vendas = Listbox(second_screen)
        for iterator in livraria.historico_de_vendas:
            historico_de_vendas.insert(END, str(iterator))
        historico_de_vendas.pack(fill = BOTH)
        
        
        
        
        
       
