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

idades.clear()
print(idades)

faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()
