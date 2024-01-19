import random 

opcoes = ['pedra', 'papel', 'tesoura', 'fim']

while True:
    jogador = input('Escolha uma opção Pedra, Papel, Tesoura ou Fim para sair: ')

    if jogador not in opcoes:
        print('Opção inválida. Tente novamente.')
    elif jogador == 'fim':
        print('Obrigado por jogar, até logo!')
        break
    else:
        computador = random.choice(opcoes)

        print('O computador escolheu {}.'.format(computador))

        if jogador == computador:
            print('Empate!')
        elif jogador == 'pedra' and computador == 'tesoura':
            print('Jogador Venceu!')
        elif jogador == 'tesoura' and computador == 'pedra':
            print('Jogador Venceu!')
        elif jogador == 'papel' and computador == 'pedra':
            print('Jogador Venceu!')
        else:
            print('Computador Venceu!')