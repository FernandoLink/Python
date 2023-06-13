from collections import defaultdict
from collections import Counter

aparicoes = {"Fernando": 53, 'Valéria': 45, 'Luiza':18,'Henrique':15,'Polly':13}
print(aparicoes)
print(type(aparicoes))
print(aparicoes['Polly'])
print(aparicoes.get('xpto', 0))
aparicoes['Arlete'] = 1
aparicoes['Valéria'] = 46
print(aparicoes)
del aparicoes['Arlete']
print(aparicoes)
print('Henrique' in aparicoes)

for elemento in aparicoes:
    print(elemento)

for elemento in aparicoes.keys():
    print(elemento)

for elemento in aparicoes.values():
    print(elemento)

for elemento in aparicoes.items():
    print(elemento)

for chave, valor in aparicoes.items():
    print(chave, '-', valor)

print([f'Nome: {chave}' for chave in aparicoes.keys()])

outro = dict(Fernando=53,Valeria=45)
print(outro)

meu_texto = "bem vindo conjuntos meu nome é Fernando Link e o nome da minha esposa é Valéria e o nome do meu cachorro é Polly o nome da minha filha é Luiza e o nome do meu filho é Henrique".lower()
print(meu_texto)
aparicoes = {}
for palavra in meu_texto.split():
    ate_agora = aparicoes.get(palavra, 0)
    aparicoes[palavra] = ate_agora + 1
print(aparicoes)    

aparicoes = defaultdict(int)
for palavra in meu_texto.split():
    ate_agora = aparicoes[palavra]
    aparicoes[palavra] = ate_agora + 1
print(aparicoes)    

aparicoes = defaultdict(int)
for palavra in meu_texto.split():
    aparicoes[palavra] += 1
print(aparicoes)    

class Conta:
  def __init__(self):
    print("Criando uma conta")

contas = defaultdict(Conta)
contas[15]

aparicoes = Counter(meu_texto.split())
print(aparicoes)    