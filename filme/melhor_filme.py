


def abrindo_arquivo():
    arquivo = open('Arquivo.csv', 'r')
    for filmes in arquivo:
        campo = filmes.strip().split(';')
        campo = [float(filmes[1]),float(filmes[2]),int(filmes[3]),float(filmes[4])]


def adicionando_filme():
    with open('Arquivo.csv', 'w') as arquivo:
        campo[filme[1]] = input("Título do filme: ", )
        filme[2] = input("Ano de lançamento: ")
        filme[3] = input("Gênero do filme: ")
        filme[1] = input("Avaliação (0 a 10): ")
        #arquivo{filme[1] = titulo}: {filme[2] =ano}; {filme[3] = genero}; {filme[4] = avaliacao} 
        arquivo.close()# Retorna o filme com a melhor avaliação
