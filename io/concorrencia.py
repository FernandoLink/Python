arquivo1 = open('io/dados/contatos-escrita.csv', mode='a')
arquivo2 = open('io/dados/contatos-escrita.csv', mode='a')

contato_carol = '11,Carol,carol@carol.com.br\n'
contato_andreza = '12,Andreza,andreza@andreza.com.br\n'

arquivo1.write(contato_carol)
arquivo2.write(contato_andreza)

arquivo1.close()
arquivo2.close()

with open('io/dados/contatos-escrita.csv', mode='a') as arquivo1:
    arquivo1.write(contato_carol)

with open('io/dados/contatos-escrita.csv', mode='a') as arquivo2:
    arquivo2.write(contato_andreza)