from fabrica_fila import FabricaFila
from estatistica_detalhada import EstatisticaDetalhada
from estatistica_resumida import EstatisticaResumida


fila_teste = FabricaFila.pega_fila('normal')
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
print(fila_teste.chama_cliente(5))
print(fila_teste.chama_cliente(10))
print(fila_teste.chama_cliente(6))
print(fila_teste.estatistica(EstatisticaResumida('24/06/2023', 120)))

fila_teste_prioritaria = FabricaFila.pega_fila('prioritaria')
fila_teste_prioritaria.atualiza_fila()
fila_teste_prioritaria.atualiza_fila()
fila_teste_prioritaria.atualiza_fila()
print(fila_teste_prioritaria.chama_cliente(5))
print(fila_teste_prioritaria.chama_cliente(10))
print(fila_teste_prioritaria.chama_cliente(7))
print(fila_teste_prioritaria.estatistica(
    EstatisticaDetalhada('24/06/2023', 120)
))
