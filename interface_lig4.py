"""Módulo que faz a interface do jogo com o usuário"""

from funcoes_lig4 import *
import random
from termcolor import colored

"""=======================================FUNÇÕES_DE_INTERFACE======================================================="""


def imprime_tabuleiro(tab):
    """Imprime o tabuleiro do jogo, desenhando a numeração, linhas e colunas
        -parametro tabuleiro: recebe a matriz do tabuleiro
        -retorna o tabuleiro construido no console"""

    for i in range(COL_TAB):
        if i != (COL_TAB - 1):
            print(i, end=" ")
        else:
            print(i)

    for lin in range(LIN_TAB):
        for c in range(COL_TAB):
            print(tab[lin][c], end="")
            if c != (COL_TAB - 1):
                print("|", end="")
        print()


def recebe_jogadores():
    """Recebe pelo console e retorna o nome dos jogadores"""

    print(colored("Insira o nome dos jogadores para iniciar o jogo.", 'green'))
    jog1 = str(input("Digite o nome do jogador 1:"))
    jog2 = str(input("Digite o nome do jogador 2:"))
    print(colored("=========================================================================================", 'green'))
    return jog1, jog2


def boas_vindas():
    """Imprime as regras do jogo Lig4 para os jogadores"""

    print(colored("=========================================================================================", 'green'))
    print(colored("                         Bem-vindo(s) ao LIG4!", 'red'))
    print(colored("Nesse jogo, você deve tentar formar uma sequência de 4 fichas da sua cor, que podem:", 'green'))
    print(colored("         -Ser na HORIZONTAL;\n         -Ser na VERTICAL;\n         -Ou na DIAGONAL.", 'green'))
    print(colored("Na sua vez, selecione uma coluna entre 0 e 6 para colocar sua ficha no tabuleiro.", 'green'))
    print(colored("Lembre-se, preste atenção para impedir que seu oponente forme uma sequência.", 'green'))
    print(colored("                          TENHA UM BOM JOGO!", 'red'))
    print(colored("=========================================================================================", 'green'))


def recebe_entrada(jogador, tab, ficha):
    """Recebe a coluna escolhida pelo jogador
        -parametro turno: recebe a identificação do jogador da vez
        -parametro tabuleiro: recebe o tabuleiro do jogo
        -retonra a coluna selecionda pelo jogador"""

    while True:
        print("vez do jogador {}.".format(jogador))
        if jogador == JOG_MAQUINA:
            coluna_selec = str(random.randrange(0, COL_TAB))
            print(colored("Jogador {} escolheu a coluna {}.", 'green').format(jogador, coluna_selec))
        else:
            coluna_selec = str(input(colored("Escolha uma coluna para colocar sua ficha {}:", 'green').format(ficha)))

        if checa_entrada(coluna_selec, tab):
            return int(coluna_selec)

        print()


def checa_entrada(coluna, tab):
    """Verifica a entrada realizada e retorna se há algum erro ou não
        -parametro jogada: recebe o valor da coluna escolhida
        -parametro tabuleiro: recebe o tabuleiro do jogo
        -retorna Verdadeiro, se as jogadas forem permitidas, ou mensagens de erro, caso haja uma jogada inválida"""

    cond_entrada = checa_jogada(coluna, tab)

    if cond_entrada == 1:
        return True

    else:
        if cond_entrada == 2:
            print(colored("\nA coluna {} está cheia, escolha outra", 'red').format(coluna))

        elif cond_entrada == 3:
            print(colored("\nColuna inválida.\nValores permitidos entre 0 e 6", 'red'))

        elif cond_entrada == 4:
            print(colored("\nJogada fora do formato correto!", 'red'))

        return False


def verifica_vencedor(tab, ficha, jogador):
    """Verifica a situação atual do tabuleiro, e retorna se houve vitória para o jogador da vez ou empate
        -parametro tabuleiro: recebe o estado atual do tabuleiro, a qual irá analisar
        -parametro ficha: recebe a ficha referente ao jogador da vez
        -parametro turno: recebe o nome do jogador da vez
        -retorna True ou False"""

    cond_tabuleiro = verifica_tabuleiro(tab, ficha)

    if cond_tabuleiro == 1:
        print(colored("\nJogador {} venceu!\nVocê formou uma linha.\n", 'green').format(jogador))
        return True

    elif cond_tabuleiro == 2:
        print(colored("\nJogador {} venceu!\nVocê formou uma coluna.\n", 'green').format(jogador))
        return True

    elif cond_tabuleiro == 3:
        print(colored("\nJogador {} venceu!\nVocê formou uma diagonal.\n", 'green').format(jogador))
        return True

    else:
        if len(jogadas_possiveis(tab)) == 0:
            print(colored("\nTodas as colunas cheias\nEmpate entre os jogadores.\n", 'green'))
            return True

        else:
            return False


"""========================================INÍCIO_DO_JOGO============================================================"""

boas_vindas()
jogador1, jogador2 = recebe_jogadores()
tabuleiro = constroi_tabuleiro()

turno = jogador1
ficha_atual = FICHA_J1

imprime_tabuleiro(tabuleiro)

while True:
    jogada = recebe_entrada(turno, tabuleiro, ficha_atual)
    faz_jogada(jogada, ficha_atual, tabuleiro)

    if verifica_vencedor(tabuleiro, ficha_atual, turno):
        imprime_tabuleiro(tabuleiro)
        break

    imprime_tabuleiro(tabuleiro)
    turno, ficha_atual = troca_turno(turno, jogador1, jogador2)
