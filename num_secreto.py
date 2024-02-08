import os
import random

def jogar():
    num_secreto = random.randrange(1, 100)

    os.system('cls')
    print('-----------------------------------')
    print('\033[92mBEM-VINDO AO JOGO DO NÚMERO SECRETO\033[0m')
    print('-----------------------------------')

    total_tentativas = 0

    print('Escolha a difuldade do jogo:\n')

    print('''\033[92m
          (1)Fácil
          (2)Médio
          (3)Difícil\033[0m\n
          ''')
    try:
        dificuldade = int(input('Dificuldade: '))

    except ValueError:
        os.system('cls')
        print('\033[91mOpção inválida\033[0m')
        print('---------------------------------')
        input('\n\033[92mPressione Enter para recomeçar...\033[0m')
        os.system('cls')
        jogar()

    if(dificuldade == 1):
        total_tentativas = 20

    elif(dificuldade == 2):
        total_tentativas = 10

    elif(dificuldade == 3):
        total_tentativas = 5

    else:
        os.system('cls')
        print('\033[91mOpção inválida\033[0m')
        print('---------------------------------')
        input('\n\033[92mPressione Enter para recomeçar...\033[0m')
        os.system('cls')
        jogar()

    tentativa_atual = total_tentativas

    condicao = tentativa_atual >= 0

    print(num_secreto)
    
    while(condicao):
        print(f'Número de tentativas restantes: \033[91m{tentativa_atual}\033[0m de {total_tentativas}\n')

        num_escolhido = int(input('Escolha um valor:\033[92m '))
        print('\033[0m')

        if(num_escolhido == num_secreto):
            print('\n\033[92mVocê acertou, parabéns!\033[0m\n')
            condicao = False
        
        elif(num_escolhido != num_secreto):
            print('Valor incorreto')
            print('---------------\n')

            if(num_escolhido > num_secreto):
                print('Tente um valor menor\n')

            elif(num_escolhido < num_secreto):
                print('Tente um valor maior\n')

            continue
        
        tentativa_atual -= 1
    



if __name__ == "__main__":
    jogar()