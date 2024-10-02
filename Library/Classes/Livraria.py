from Classes import * 

from .HistoricoDeVendas import *

from Exceptions import *
from tkinter import messagebox

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

