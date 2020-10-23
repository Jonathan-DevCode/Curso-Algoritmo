def usuario_escolhe_jogada(total_pecas, limite):
    total_pecas = int(input('Quantas peças você vai tirar? '))
    while total_pecas > limite:
        print('Oops! Jogada inválida! Tente de novo.')
        print()
        total_pecas = int(input('Quantas peças você vai tirar? '))

    while total_pecas <= 0:
        print('Oops! Jogada inválida! Tente de novo.')
        print()
        total_pecas = int(input('Quantas peças você vai tirar? '))

    limite = total_pecas

    return limite


def computador_escolhe_jogada(total_pecas, limite):
    referencia = limite
    copia_total = total_pecas

    while total_pecas % (referencia + 1) != 0:
        if limite == 0:
            break
        else:
            limite = limite - 1
            total_pecas = copia_total - (limite + 1)

    if referencia != limite:
        limite = limite + 1

    return limite


def partida():
    global computador
    global player

    total_pecas = int(input('Quantas peças? '))
    limite = int(input('Limite de peças por jogada? '))
    escolha = 0

    while total_pecas != 0:
        if computador == 0 and player == 0:
            n3 = total_pecas % (limite + 1)
            if n3 == 0:
                print()
                print('Você começa', '\n')
                computador = computador + 1
            else:
                player = player + 1

        if computador > player:
            escolha = usuario_escolhe_jogada(total_pecas, limite)
            total_pecas = total_pecas - escolha
            player = player + 1
            if player == computador:
                player = player + 1

            if total_pecas > 1:
                print('Agora restam', total_pecas, 'peças no tabuleiro', '\n')
            elif total_pecas == 1:
                print('Agora resta apenas', total_pecas, 'peça no tabuleiro', '\n')

        else:
            escolha = computador_escolhe_jogada(total_pecas, limite)
            total_pecas = total_pecas - escolha
            computador = computador + 1
            if computador == player:
                computador = computador + 1

            if total_pecas >= 2:
                if escolha == 1:
                    print('O computador tirou', escolha, 'peça')
                    print('Agora restam', total_pecas, 'peças no tabuleiro', '\n')
                else:
                    print('O computador tirou', escolha, 'peças')
                    print('Agora restam', total_pecas, 'peças no tabuleiro', '\n')
            elif total_pecas <= 0:
                if escolha == 1:
                    print('O computador tirou', escolha, 'peça')
                    print('Fim do jogo! O computador ganhou!', '\n')
                elif total_pecas < 0:
                    total_pecas = 0
                else:
                    print('O computador tirou', escolha, 'todas as peças')
                    print('Fim do jogo! O computador ganhou!', '\n')


def campeonato():
    global computador, player
    placar_cpu = 0

    while placar_cpu != 3:
        partida()
        placar_cpu = placar_cpu + 1
        print('Placar: Você 0 X', placar_cpu, 'Computador')
        print()
        computador = 0
        player = 0


print('Bem-vindo ao jogo do NIM! Escolha: ')
print('1 - jogar partida isolada ')
print('2 - para jogar um campeonato ')
opcao = int(input())
computador = 0
player = 0

while opcao != 1 or opcao != 2:
    if opcao == 1:
        partida()
        break
    elif opcao == 2:
        campeonato()
    else:
        print('Ops! Não existe essa opção, por favor digite 1 para partida ou 2 para campeonato')
        opcao = int(input())
