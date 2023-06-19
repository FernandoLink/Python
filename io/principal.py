import contato_util

try:
    contatos = contato_util.csv_para_contatos('io/dados/contatos.csv')
    for contato in contatos:
        print(f'{contato.id} - {contato.nome} - {contato.email}')

    contato_util.contatos_para_pickle(contatos, 'io/dados/contatos.pickle')

    contatos = contato_util.pickle_para_contatos('io/dados/contatos.pickle')
    for contato in contatos:
        print(f'{contato.id} - {contato.nome} - {contato.email}')

    contato_util.contatos_para_json(contatos, 'io/dados/contatos.json')

    contatos = contato_util.json_para_contatos('io/dados/contatos.json')
    for contato in contatos:
        print(f'{contato.id} - {contato.nome} - {contato.email}')

except FileNotFoundError:
    print('Arquivo não encontrado')
except PermissionError:
    print("Sem permissão de escrita")    