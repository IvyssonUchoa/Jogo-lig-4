"""Módulo que mantém as constantes do jogo"""

from termcolor import colored

"""=======================CONSTANTES================================================================================="""

LIN_TAB = 6
COL_TAB = 7
FICHA_VENC_J1 = colored("●", 'yellow')
FICHA_VENC_J2 = colored("●", 'yellow')
FICHA_J1 = colored("●", 'red')
FICHA_J2 = colored("●", 'blue')
ESPACO_VAZIO = "_"
COL_PERMITIDAS = ["0", "1", "2", "3", "4", "5", "6"]
SEQ_MINIMA = 4
MIN_DIAG_1 = 3
MAX_DIAG_1 = 8
MIN_DIAG_2 = -3
MAX_DIAG_2 = 2
JOG_MAQUINA = "BOT"
