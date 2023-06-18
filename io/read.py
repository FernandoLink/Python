try:
    with open('io/dados/contatos.csv') as contatos:
        for linha in contatos.readlines():
            print(linha, end='')
        contatos.seek(0)
        print(contatos.readline())
except FileNotFoundError:
    print('Arquivo não encontrado')
except PermissionError:
    print("Sem permissão de escrita")
