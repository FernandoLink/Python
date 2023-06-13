# Lista são mutáveis

def faz_processamento_de_visualizacao(lista = None):
    if lista == None:
        lista = list()
    print(len(lista))
    lista.append(13)

idades = [53, 46, 18,15]
print(type(idades))
print(idades)
print(len(idades))
print(idades[3])
print(idades[1:])
print(idades[:2])
idades.append(26)
print(idades)
idades.remove(26)
for idade in idades:
    print(idade)

print(53 in idades)

idades.insert(0, 20)
print(idades)

idades.extend([65,78,69,50])
print(idades)

print([(idade+1) for idade in idades])

print([(idade+1) for idade in idades if idade > 21])

for i in range(len(idades)):
    print(i, idades[i])

print(list(enumerate(idades)))    

for indice, idade in enumerate(idades):
    print(indice, idade)

print(list(reversed(idades)))
print(sorted(idades, reverse=True))
print(list(reversed(sorted(idades))))

# Lembre-se list é mutável
idades.sort()
print(idades)

idades.clear()
print(idades)

faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()

usuarios = [('Fernando', 53, 1970),('Valéria',46,1975),('Luiza', 18, 2005),('Henrique',15,2007)]
for nome, _, _ in usuarios:
    print(nome)

