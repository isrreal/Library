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

class HistoricoDeVendas:
    def __init__(self):
        self.__historico = []
    @property
    def historico(self):
        return self.__historico
    def push(self, venda):
        self.__historico.append(venda) 

class Venda:
    identificador = 0
    def __init__(self, venda):
        Venda.identificador += 1
        self.identificador = Venda.identificador
        self.venda = venda
    def __str__(self):
        return f"identificador da venda: {self.identificador}   {self.venda}"
    
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
    
class LivroDeAventura(Livro):
    def __init__(self, titulo, quantidade):
        super().__init__(titulo, random.randrange(20, 70), quantidade, tipo = "Aventura")

class LivroDeComedia(Livro):
    def __init__(self, titulo, quantidade):
        super().__init__(titulo, random.randrange(20, 70), quantidade, tipo = "Comédia")

class LivroDeDrama(Livro):
    def __init__(self, titulo, quantidade):
        super().__init__(titulo, random.randrange(20, 70), quantidade, tipo = "Drama")

class Livraria:
    def __init__(self, capital):
        self.__taxa_de_lucro = 0.75
        self.__montante = capital
        self.__estoque_de_livros = []
        self.__historico_de_vendas = HistoricoDeVendas()
    def __adicionar_em_historico(self, venda: Venda):
        self.__historico_de_vendas.push(venda)
    def __adicionar_livro(self, livro, quantidade):
        if livro not in self.__estoque_de_livros:
            self.__estoque_de_livros.append(livro)
            self.__estoque_de_livros.sort(key = lambda x: x.tipo)
        else:
            self.__estoque_de_livros[self.__estoque_de_livros.index(livro)].quantidade = quantidade
    @property
    def montante(self):
        return self.__montante
    @property
    def taxa_de_lucro(self):
        return self.__taxa_de_lucro
    @property
    def historico_de_vendas(self):
        return self.__historico_de_vendas.historico
    @property
    def estoque(self):
        return self.__estoque_de_livros
    def comprar_livro(self, livro):
        if self.montante - livro.quantidade * (livro.valor) >= 0:
            self.__montante -= livro.quantidade * livro.valor
            self.__adicionar_livro(livro, livro.quantidade)
            messagebox.showinfo("Comprar Livro", "Livro comprado com sucesso!")
        else:
            raise CapitalInsuficiente("Não há capital o suficiente para a realização dessa compra.")
    def vender_livro(self, livro, quantidade):
        if self.__estoque_de_livros[self.__estoque_de_livros.index(livro)].quantidade - quantidade < 0:
            raise VendasExcedemLimite("Quantidade de livros menor do que a se vender!")
        elif self.__estoque_de_livros[self.__estoque_de_livros.index(livro)].quantidade - quantidade > 0:
            self.__montante += quantidade * livro.valor * self.taxa_de_lucro
            self.__estoque_de_livros[self.__estoque_de_livros.index(livro)].quantidade = -quantidade
            self.__historico_de_vendas.push(Venda(f"{livro}     - quantidade vendida: {quantidade}   - lucro: R$ {quantidade * livro.valor * self.taxa_de_lucro}  "))
            messagebox.showinfo("Vender livro", "Livro vendido com sucesso!")
        elif self.__estoque_de_livros[self.__estoque_de_livros.index(livro)].quantidade - quantidade == 0:
            self.__montante += livro.quantidade * livro.valor * self.taxa_de_lucro
            self.__estoque_de_livros.remove(livro)  
            self.__historico_de_vendas.push(Venda(f"{livro}- quantidade vendida: {quantidade}  - lucro: R$ {quantidade * livro.valor * self.taxa_de_lucro} "))
            messagebox.showinfo("Vender livro", "Livro vendido com sucesso!")
            messagebox.showwarning("Vender livro", f"Estoque do livro: \"{livro.titulo}\"\nidentificador \"{livro.identificador}\" acabou de ser esgotado!")


def copiar_identificador(lista):
    window.clipboard_clear()
    valores = lista.curselection()
    if lista:
        id = re.findall("[0-9]+", lista.get(valores[0]))[0]
        window.clipboard_append(id)
        messagebox.showinfo("Copiar identificador", "Identificador copiado com sucesso!")

def switch_type(tipo, second_screen):
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
    botao_confirma = Button(moldura, text = "Confirmar", command = partial(switch_type, valor, second_screen)).pack()

def vender_livro(livraria: Livraria):
    identificador_do_livro = simpledialog.askstring("Vender livro", "Digite o idenfificador do livro a se vender")
    quantidade = simpledialog.askinteger("Vender livro", "Digite a quantidade a se vender")
    book = list(filter(lambda x: x.identificador == identificador_do_livro, livraria.estoque))
    raise LivroInexistente("O livro a se vender não existe no estoque!") if not book else livraria.vender_livro(book[0], quantidade) 

def consultar_estoque(livraria: Livraria):
    if not livraria.estoque:
        messagebox.showinfo("Estoque", "Não há livros no estoque")
    else:
        second_screen = Tk()
        second_screen.title("Estoque")
        lista = Listbox(second_screen)
        for iterator in livraria.estoque:
            lista.insert(END, str(iterator))
        lista.pack(fill = BOTH, expand = True)
        botao_copiar_identificador = Button(second_screen, text = "Copiar Identificador", command = partial(copiar_identificador, lista)).pack()

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


if __name__ == '__main__':
    try:
        window = Tk()
        window.configure(bg = "#F3C3BA")
        window.title("Livraria")      
        window.geometry("720x480")
        window.maxsize(720, 480)
        livraria = Livraria(8000)
        options = Label(window, text = ''' 
                    Selecione uma das opções: 
                        - Adicionar livro
                        - Vender livro
                        - Consultar estoque"
                        - Consultar montante"
                        - Consultar historico de vendas
                    ''', bd = 51, bg = "#E6D8BF", font = "arial")
        options.pack(side = LEFT)
        container = Frame(window, bg = "#E6D8BF", bd = 50)
        container.pack(side = LEFT)
        comprar_livro = Button(container, text = "Comprar livro", command = partial(comprar_livro, livraria))
        vender_livro = Button(container, text = "Vender livro", command = partial(vender_livro, livraria))
        consultar_estoque = Button(container, text = "Consultar estoque", command = partial(consultar_estoque, livraria))
        consultar_historico_de_vendas = Button(container, text = "Consultar histórico de vendas", command = partial(consultar_historico_de_vendas, livraria))
        consultar_montante = Button(container, text = "Consultar montante", command = partial(consultar_montante, livraria))
        comprar_livro.grid(row = 0, column = 0)
        vender_livro.grid(row = 1, column = 0)
        consultar_estoque.grid(row = 2, column = 0)
        consultar_historico_de_vendas.grid(row = 3, column = 0)
        consultar_montante.grid(row = 4, column = 0)     
        window.mainloop()
    except:
        print("Um erro ocorreu.")
