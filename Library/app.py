from tkinter import simpledialog
from tkinter import messagebox
from tkinter import Button
from tkinter import Label 
from tkinter import Frame 
from tkinter import *

from functools import partial

from Classes import *
from Utils import *

if __name__ == '__main__':
    window = Tk()
    window.configure(bg = "#F3C3BA")
    window.title("Livraria")      
    window.geometry("720x480")
    window.maxsize(720, 480)

    # Usando grid para controlar a posição do frame
    window.grid_columnconfigure(0, weight=1)

    # Frame único para a label de opções e os botões
    container_frame = Frame(window, bg="#F3C3BA")
    container_frame.grid(row=0, column=0, padx=10, pady=20, sticky="n")

    livraria = Livraria(8000)

    # Label com as opções
    options = Label(container_frame, text="Selecione uma das opções:", bd=10, bg="#E6D8BF", font="arial")
    options.grid(row=0, column=0, columnspan=2, pady=10)

    # Botões abaixo da Label, ainda no mesmo frame
    comprar_livro = Button(container_frame, text="Comprar livro", command=partial(comprar_livro, livraria))
    vender_livro = Button(container_frame, text="Vender livro", command=partial(vender_livro, livraria))
    consultar_estoque = Button(container_frame, text="Consultar estoque", command=partial(consultar_estoque, livraria, window))
    consultar_historico_de_vendas = Button(container_frame, text="Consultar histórico de vendas", command=partial(consultar_historico_de_vendas, livraria))
    consultar_montante = Button(container_frame, text="Consultar montante", command=partial(consultar_montante, livraria))

    # Disposição dos botões abaixo da label usando grid
    comprar_livro.grid(row=1, column=0, pady=5, sticky="w")
    vender_livro.grid(row=2, column=0, pady=5, sticky="w")
    consultar_estoque.grid(row=3, column=0, pady=5, sticky="w")
    consultar_historico_de_vendas.grid(row=4, column=0, pady=5, sticky="w")
    consultar_montante.grid(row=5, column=0, pady=5, sticky="w")

    window.mainloop()

