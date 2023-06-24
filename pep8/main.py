from fila_prioritaria import FilaPrioritaria
from fila_normal import FilaNormal


fila_teste = FilaNormal()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
print(fila_teste.chama_cliente(5))
print(fila_teste.chama_cliente(10))
print(fila_teste.chama_cliente(6))

fila_teste_prioritaria = FilaPrioritaria()
fila_teste_prioritaria.atualiza_fila()
fila_teste_prioritaria.atualiza_fila()
fila_teste_prioritaria.atualiza_fila()
print(fila_teste_prioritaria.chama_cliente(5))
print(fila_teste_prioritaria.chama_cliente(10))
print(fila_teste_prioritaria.chama_cliente(7))
print(fila_teste_prioritaria.estatistica('10/01/2023', 198, 'detail'))
