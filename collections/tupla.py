# Tuplas são imutáveis

conta = (15, 1000)
print(type(conta))
print(conta)
print(conta[1])

link = ('Fernando Link', 53)
val = ('Valeria Cristina Souza Link', 46)
luiza = ('Luiza Souza Link', 18)
henrique = ('Henrique Souza Link', 15)

familia = [link, val, luiza]
print(familia)
familia.append(henrique)
print(familia)
print(familia[1][1])