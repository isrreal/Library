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
