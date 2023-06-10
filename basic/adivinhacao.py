import random

def jogar():
    print('*********************************')
    print('Bem vindo ao jogo de Adivinhação!')
    print('*********************************')
    print('Qual nível de dificuldade? (1) Fácil (2) Médio (3) Difícil')
    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    numero_secreto = random.randrange(1, 101)
    pontos = 1000

    for rodada in range(1, total_de_tentativas + 1):
        print('Tentativas {1} de {0}'.format(total_de_tentativas, rodada))
        chute_str = input('Digite um número entre 1 e 100: ')
        print('Você digitou ', chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print('Você deve digitar um número entre 1 e 100: ')
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print('Você acertou.')
            print(f'Parabéns! {"Fernando Link"} você ganhou R$ {pontos:.2f} em {rodada} tentativas.')
            break
        else:
            if(maior):
                print('Você errou! O seu chute foi maior que o número secreto.')
            elif(menor):
                print('Você errou! O seu chute foi menor que o número secreto.')
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

        rodada = rodada + 1

    print('Fim do jogo.')    

if(__name__ == "__main__"):
    jogar()    
