arquivo = open('io/dados/contatos.csv')

print(type(arquivo.buffer))
print(type(arquivo.buffer.read()))

arquivo.seek(0)
conteudo = arquivo.buffer.read()
print(conteudo)

texto_em_bytes = b'Esse eh um texto em bytes'
print(type(texto_em_bytes))
print(texto_em_bytes)

texto_em_bytes = bytes('Esse é um texto em bytes', 'UTF_8')
print(type(texto_em_bytes))
print(texto_em_bytes)

arquivo.close()
