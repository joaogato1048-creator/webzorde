import csv

ARQUIVO = "filmes.csv"

# Carrega os filmes do arquivo CSV
def carregar_filmes():
    filmes = []
    try:
        with open(ARQUIVO, newline='', encoding='utf-8') as f:
            leitor = csv.DictReader(f) # caminho para ler o arquivo CSV como dicionário
            for linha in leitor:
                filmes.append(linha)
    except FileNotFoundError:
        pass
    return filmes # se o arquivo não eexistir, retorna lista vazia

# Salva os filmes no arquivo CSV
def salvar_filmes(filmes):
    with open(ARQUIVO, 'w', newline='', encoding='utf-8') as f:
        campos = ['título', 'ano', 'gênero', 'avaliação']
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(filmes)

# Lista todos os filmes
def listar_filmes(filmes):
    print("\n--- Filmes em catálogo ---")
    if not filmes:
        print("Nenhum filme cadastrado.\n")
    else:
        for f in filmes:
            print(f"{f['título']} ({f['ano']}) - {f['gênero']} - Avaliação: {f['avaliação']}")
        print()

# Busca filmes por gênero
def buscar_por_genero(filmes):
    genero = input("Digite o gênero: ").strip().lower()
    encontrados = [f for f in filmes if f['gênero'].lower() == genero]
    print()
    if encontrados:
        for f in encontrados:
            print(f"{f['título']} ({f['ano']}) - Avaliação: {f['avaliação']}")
    else:
        print("Nenhum filme encontrado nesse gênero.")
    print()

# Busca filmes por ano
def buscar_por_ano(filmes):
    ano = input("Digite o ano: ").strip()
    encontrados = [f for f in filmes if f['ano'] == ano]
    print()
    if encontrados:
        for f in encontrados:
            print(f"{f['título']} - {f['gênero']} - Avaliação: {f['avaliação']}")
    else:
        print("Nenhum filme encontrado nesse ano.")
    print()

# Adiciona um novo filme
def adicionar_filme(filmes):
    titulo = input("Título: ")
    ano = input("Ano: ")
    genero = input("Gênero: ")
    avaliacao = input("Avaliação (0 a 10): ")
    filmes.append({'título': titulo, 'ano': ano, 'gênero': genero, 'avaliação': avaliacao})
    salvar_filmes(filmes)
    print("Filme adicionado com sucesso!\n")

# Calcula a média das avaliações
def calcular_media_avaliacoes(filmes):
    if not filmes:
        print("Nenhum filme cadastrado.\n")
        return
    notas = [float(f['avaliação']) for f in filmes]
    media = sum(notas) / len(notas)
    print(f"Média das avaliações: {media:.2f}\n")

# Menu principal
def menu():
    filmes = carregar_filmes()
    while True:
        print("""
===== CATÁLOGO DE FILMES =====
1 - Listar todos os filmes
2 - Buscar por gênero
3 - Buscar por ano
4 - Adicionar novo filme
5 - Calcular média das avaliações
0 - Sair
""")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            listar_filmes(filmes)
        elif opcao == '2':
            buscar_por_genero(filmes)
        elif opcao == '3':
            buscar_por_ano(filmes)
        elif opcao == '4':
            adicionar_filme(filmes)
        elif opcao == '5':
            calcular_media_avaliacoes(filmes)
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida.\n")

menu()