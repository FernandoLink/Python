alunos1 = [13,15,26,74,86]
alunos2 = [13,17,26,75,87]

alunos = alunos1.copy()
alunos.extend(alunos2)

print(alunos)
print(set(alunos))
print({4,3,2,1,2,3,4,5})

for aluno in set(alunos):
    print(aluno)

alunos1 = {13,15,26,74,86}
alunos2 = {13,17,26,75,87}

print(alunos1 | alunos2)    
print(alunos1 & alunos2)    
print(alunos1 - alunos2)
print(alunos1 ^ alunos2)

print(15 in alunos1)
print(15 in alunos2)

alunos1.add(14)
print(alunos1)

alunos_frozen = frozenset(alunos1)
print(alunos_frozen)

meu_texto = "bem vindo conjuntos meu nome é Fernando Link e o nome da minha esposa é Valéria e o nome do meu cachorro é Polly o nome da minha filha é Luiza e o nome do meu filho é Henrique"
print(meu_texto)
palavras_do_texto_sem_duplicaidade = set(meu_texto.split())
print(palavras_do_texto_sem_duplicaidade)