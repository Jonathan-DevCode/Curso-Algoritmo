def usuario_escolhe_jogada(qtpecas, limtotal):
    qtpecas = int(input('Quantas peças você vai tirar? '))
    while qtpecas > limtotal:
        print('Oops! Jogada inválida! Tente de novo.')
        print()
        qtpecas = int(input('Quantas peças você vai tirar? '))

    while qtpecas <= 0:
        print('Oops! Jogada inválida! Tente de novo.')
        print()
        qtpecas = int(input('Quantas peças você vai tirar? '))

    limtotal = qtpecas

    return limtotal


def computador_escolhe_jogada(qtpecas, limtotal):
    n2 = limtotal
    copypecas = qtpecas

    while qtpecas % (n2 + 1) != 0:
        if limtotal == 0:
            break
        else:
            limtotal = limtotal - 1
            qtpecas = copypecas - (limtotal + 1)

    if n2 != limtotal:
        limtotal = limtotal + 1

    return limtotal


def partida():
    global nac
    global nap

    qtpecas = int(input('Quantas peças? '))
    limtotal = int(input('Limite de peças por jogada? '))
    p = 0

    while qtpecas != 0:
        if nac == 0 and nap == 0:
            n3 = qtpecas % (limtotal + 1)
            if n3 == 0:
                print()
                print('Você começa', '\n')
                nac = nac + 1
            else:
                nap = nap + 1

        if nac > nap:
            p = usuario_escolhe_jogada(qtpecas, limtotal)
            qtpecas = qtpecas - p
            nap = nap + 1
            if nap == nac:
                nap = nap + 1

            if qtpecas > 1:
                print('Agora restam', qtpecas, 'peças no tabuleiro', '\n')
            elif qtpecas == 1:
                print('Agora resta apenas', qtpecas, 'peça no tabuleiro', '\n')

        else:
            p = computador_escolhe_jogada(qtpecas, limtotal)
            qtpecas = qtpecas - p
            nac = nac + 1
            if nac == nap:
                nac = nac + 1

            if qtpecas >= 2:
                if p == 1:
                    print('O computador tirou', p, 'peça')
                    print('Agora restam', qtpecas, 'peças no tabuleiro', '\n')
                else:
                    print('O computador tirou', p, 'peças')
                    print('Agora restam', qtpecas, 'peças no tabuleiro', '\n')
            elif qtpecas <= 0:
                if p == 1:
                    print('O computador tirou', p, 'peça')
                    print('Fim do jogo! O computador ganhou!', '\n')
                elif qtpecas < 0:
                    qtpecas = 0
                else:
                    print('O computador tirou', p, 'todas as peças')
                    print('Fim do jogo! O computador ganhou!', '\n')


def campeonato():
    global nac, nap
    pcpu = 0

    while pcpu != 3:
        partida()
        pcpu = pcpu + 1
        print('Placar: Você 0 X', pcpu, 'Computador')
        print()
        nac = 0
        nap = 0


print('Bem-vindo ao jogo do NIM! Escolha: ')
print('1 - jogar partida isolada ')
print('2 - para jogar um campeonato ')
var = int(input())
nac = 0
nap = 0

while var != 1 or var != 2:
    if var == 1:
        partida()
        break
    elif var == 2:
        campeonato()
    else:
        print('Ops! Não existe essa opção, por favor digite 1 para partida ou 2 para campeonato')
        var = int(input())
