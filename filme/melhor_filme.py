



arquivo = open('Arquivo.csv', 'w')
for filmes in arquivo:
    campo = filmes.strip().split(';')
    campo = [float(filmes[1]),float(filmes[2]),int(filmes[3]),float(filmes[4])]






arquivo.close()