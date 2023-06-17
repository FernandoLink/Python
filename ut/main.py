from codigo.bytebank import Funcionario

def teste_idade():
    funcionario_teste = Funcionario('Teste', '22/04/1970', 1111)
    print(f'Teste = {funcionario_teste.idade()}')

link = Funcionario('Fernando Link', '22/04/1970', 1000)
print(link.idade())

teste_idade()

ana = Funcionario('Ana', '12/03/1997', 1000000)
print(ana.calcular_bonus())
