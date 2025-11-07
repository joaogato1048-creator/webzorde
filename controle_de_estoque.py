#1. Sistema de Controle de Estoque (CSV)
#Desenvolva um programa em Python para gerenciar o estoque de uma pequena loja. O sistema deve ler e gravar os dados em um arquivo CSV contendo informações sobre os produtos (código, nome, quantidade e preço unitário). O programa deve permitir, via console:

#Listar todos os produtos em estoque;
#Adicionar um novo produto;
#Atualizar a quantidade ou o preço de um produto existente;
#Remover um produto;
#Calcular e exibir o valor total do estoque.
#O arquivo deve ser atualizado automaticamente a cada operação. 


from tkinter import*
root=Tk()

root.geometry ("3000x700")
root.title("Myapp")
root.config(bg="black")
root.mainloop()

def svr():
    estoque = 50
    QTD_PD = 50
    produtos = {
                1:["Borracha", 7.8],
                2:["Lápis", 2.75],
                3:["Caderno 100fls", 13.23],
                4:["Refrigerante 310ml", 5]
            }
    for a in range(estoque):
       print(f"{QTD_PD}, {produtos} {1} {2}")

def banco_de_dados():
    import sqlite3
    print("SQLite funciona!")