"""Módulo com funções que operam, controlam e verificam o jogo"""

from constantes import *

"""=====================================FUNÇÕES_DO_JOGO=============================================================="""


def constroi_tabuleiro():
    """Cria um tabuleiro a partir de uma matriz de tamanho constante
        -retorna o tabuleiro construido"""

    tabuleiro = list()
    for lin in range(LIN_TAB):
        linha_tab = list()
        for c in range(COL_TAB):
            linha_tab.append(ESPACO_VAZIO)
        tabuleiro.append(linha_tab)

    return tabuleiro


def troca_turno(turno, j1, j2):
    """Troca o turno entre os jogadores
        -parametro turno: recebe o turno atual
        -parametro ficha: recebe a ficha referente ao jogador atual
        -parametro j1 e j2: Recebe os nomes dos jogadores 1 e 2
        -retorna o  nome e a ficha do jogodar do novo turno"""

    if turno == j1:
        ficha = FICHA_J2
        turno = j2
    else:
        turno = j1
        ficha = FICHA_J1

    return turno, ficha


def faz_jogada(jogada, ficha, tabuleiro):
    """Coloca a ficha do jogador atual no tabuleiro
        -parametro jogada: Recebe a coluna escolhida para colocar a ficha
        -parametro turno: recebe o jogador da vez
        -Não há retorno. Altera a situação do tabuleiro, acrescentando uma ficha"""

    for lin in range(LIN_TAB - 1, -1, -1):
        if tabuleiro[lin][jogada] == ESPACO_VAZIO:
            tabuleiro[lin][jogada] = ficha
            break


def checa_jogada(coluna, tabuleiro):
    """Verifica se o a coluna selecinada é válida
        -parametro jogada: recebe o valor da coluna escolhida
        -parametro tabuleiro: recebe o tabuleiro do jogo
        -retorna um valor referente a cada tipo de saída possível"""

    try:
        if coluna in COL_PERMITIDAS:
            coluna = int(coluna)
            if tabuleiro[0][coluna] == ESPACO_VAZIO:
                return 1
            else:
                return 2

        elif int(coluna) < 0 or int(coluna) >= COL_TAB:
            return 3

    except ValueError:
        return 4

    return False


def verifica_linhas(tabuleiro, ficha):
    """Verifica as linhas do tabuleiro, identificando se o jogador alinhou 4 fichas na horizontal
        -parametro tabuleiro: recebe o tabuleiro do jogo para avaliar suas linhas
        -parametro ficha: recebe a ficha do jogador a qual irá procurar
        -Retorna se foi formado ou não uma seguencia com as fichas do jogador atual"""

    for i in range(LIN_TAB - 1, -1, -1):
        contador_sequencial = 0
        local_fichas = []

        for j in range(COL_TAB):
            if tabuleiro[i][j] == ficha:
                contador_sequencial += 1
                local_fichas.append(i)
                local_fichas.append(j)
            else:
                contador_sequencial = 0
                local_fichas = []

            if contador_sequencial == SEQ_MINIMA:
                colore_pecas(tabuleiro, ficha, local_fichas)
                return True


def verifica_colunas(tabuleiro, ficha):
    """Verifica as linhas do tabuleiro, identificando se o jogador alinhou 4 fichas na vertical
            -parametro tabuleiro: recebe o tabuleiro do jogo para avaliar suas linhas
            -parametro ficha: recebe a ficha do jogador a qual irá procurar
            -Retorna se foi formado ou não uma seguencia com as fichas do jogador atual"""

    for i in range(COL_TAB):
        contador_sequencial = 0
        local_fichas = []

        for j in range(LIN_TAB-1, -1, -1):
            if tabuleiro[j][i] == ficha:
                contador_sequencial += 1
                local_fichas.append(j)
                local_fichas.append(i)
            else:
                contador_sequencial = 0
                local_fichas = []

            if contador_sequencial == SEQ_MINIMA:
                colore_pecas(tabuleiro, ficha, local_fichas)
                return True


def verifica_diagonal_crescente(tabuleiro, ficha):
    """Verifica as diagonais crescentes do tabuleiro, identificando se o jogador alinhou 4 fichas
            -parametro tabuleiro: recebe o tabuleiro do jogo para avaliar suas linhas
            -parametro ficha: recebe a ficha do jogador a qual irá procurar
            -Retorna se foi formado ou não uma seguencia com as fichas do jogador atual"""

    for chave in range(MIN_DIAG_1, MAX_DIAG_1+1):
        contador_sequencial = 0
        local_fichas = []

        for i in range(LIN_TAB):

            for j in range(COL_TAB):

                if i + j == chave:
                    if tabuleiro[i][j] == ficha:
                        contador_sequencial += 1
                        local_fichas.append(i)
                        local_fichas.append(j)
                    else:
                        contador_sequencial = 0
                        local_fichas = []

                    if contador_sequencial == SEQ_MINIMA:
                        colore_pecas(tabuleiro, ficha, local_fichas)
                        return True


def verifica_diagonal_decrescente(tabuleiro, ficha):
    """Verifica as diagonais decrescentes do tabuleiro, identificando se o jogador alinhou 4 fichas
                -parametro tabuleiro: recebe o tabuleiro do jogo para avaliar suas linhas
                -parametro ficha: recebe a ficha do jogador a qual irá procurar
                -Retorna se foi formado ou não uma seguencia com as fichas do jogador atual"""

    for chave in range(MIN_DIAG_2, MAX_DIAG_2+1):
        contador_sequencial = 0
        local_fichas = []

        for i in range(LIN_TAB):

            for j in range(COL_TAB):

                if i - j == chave:
                    if tabuleiro[i][j] == ficha:
                        contador_sequencial += 1
                        local_fichas.append(i)
                        local_fichas.append(j)
                    else:
                        contador_sequencial = 0
                        local_fichas = []

                    if contador_sequencial == SEQ_MINIMA:
                        colore_pecas(tabuleiro, ficha, local_fichas)
                        return True


def jogadas_possiveis(tabuleiro):
    """"Identifica e retorna as colunas que permacem vazias no tabuleiro
        -Parametro tabuleiro: recebe a situação atual do tabuleiro
        -Retorna uma lista com as culonas que ainda estão vazias"""

    col_vazias = []
    for c in range(COL_TAB):
        if tabuleiro[0][c] == ESPACO_VAZIO:
            col_vazias.append(c)
    return col_vazias


def colore_pecas(tabuleiro, ficha, localizacoes):
    """Recebe e colore as peças do jogador vencedor, detacando a coluna, linha ou diagonal formada
        -Parametro tabuleiro: recebe a condição final do tabuleiro
        -Parametro ficha: recebe a ficha referente ao vencedor da partida
        -Parametro localizações: Recebe as coordenadas das fichas do jogador vencedor
        -Não há retorno. Altera as fichas dentro do tabuleiro"""

    if ficha == FICHA_J1:
        ficha_vencedor = FICHA_VENC_J1
    else:
        ficha_vencedor = FICHA_VENC_J2

    contador = 0
    for i in range(SEQ_MINIMA):
        tabuleiro[localizacoes[contador]][localizacoes[contador+1]] = ficha_vencedor
        contador += 2


def verifica_tabuleiro(tabuleiro, ficha):
    """Verifica as condições de vitória ou empate para o jogo
        -parametro tabuleiro: recebe o estado atual do tabuleiro, a qual irá analisar
        -parametro ficha: recebe a ficha referente ao jogador da vez
        -retorna 1 para vitória por sequência horizontal
        -retorna 2 para vitória por sequência vetical
        -retorna 3 para vitória por sequência diagonal
        -retorna 4 para empata
        -retorna 0 caso não haja vitória ou empate"""

    if verifica_linhas(tabuleiro, ficha):
        return 1

    elif verifica_colunas(tabuleiro, ficha):
        return 2

    elif (verifica_diagonal_crescente(tabuleiro, ficha)) or (verifica_diagonal_decrescente(tabuleiro, ficha)):
        return 3

    else:
        return 0
