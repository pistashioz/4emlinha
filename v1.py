#tabuleiro 7x6
#tem de colocar 4 fichas seguidas na horizonta, vertical ou diagonal
import os
import random

def criarTabuleiro(nlin, ncol):
    tabuleiro = []
    for i in range(nlin):     
        tabuleiro.append([])             # acrescenta uma lista vazia para cada coluna
        for j in range(ncol):   
            tabuleiro[i].append('|  |')

    for i in range(nlin):
        for j in range(ncol):
            print( tabuleiro[i][j], end="\t")
        print("\n")
    input()
    return tabuleiro

def cabecalho():
    os.system("cls")
    print()
    print()
    print("1 \t 2 \t 3 \t 4 \t 5 \t 6 \t 7")
    print("----------------------------------------------------")
    criarTabuleiro(6,7)

def comprovarSeleçao(tabuleiro):
    colunas = [1, 2, 3, 4, 5, 6, 7]
    coluna = int(input("escolha uma coluna: "))
    while True: 
        if coluna not in colunas:
            print("o espaço dado nao existe no tabuleiro!")
            input()
            break
        elif tabuleiro[0][coluna-1] != 0:
            print('espaço ocupado')
        else:
            return coluna - 1


                
def obterPosicaoValida(coluna, tabuleiro):
    linha = len(tabuleiro) - 1 
    while linha >= 0:
        if tabuleiro[linha][coluna] == 0:
            return fila
        fila =-1
    return -1

def versao1(player1, player2):
    cabecalho()
    comprovarSeleçao(tabuleiro)
    obterPosicaoValida(coluna, tabuleiro)

def colocarPeça(coluna, turno, tabuleiro):
    if turno == player1:
        peça = x
    else:
        peça = o
    fila = obterPosicaoValida(coluna, tabuleiro)
    if fila == -1:
        return False
    tabuleiro[fila][coluna] = peça
    return True

def obterConteio(fila, coluna, peça, tabuleiro):
    #hmmmmmmmmmm
    a 

def obterPeça(turno):
    if turno == player1:
        peça = x
    else:
        peça = 0
    return peça

def winner(turno, tabuleiro):
    peça = obterPeça(turno)
    for f, fila in enumerate(tabuleiro):
        for c, celda in enumerate(fila):
            conteio = obterConteio(f, c, peça, tabuleiro)
            if conteio >= conecta:
                return True 
    return False

def versao2(player):
    cabecalho()


def escolherPlayer():
    turno =  random.choice(player1, player2)
    return turno



opcao = 9
while opcao != 0:
    os.system("cls")
    print("MENU \n 1 - Player1 vs Player2 \n 2 - Player vs computador  \n 0 - Sair")
    opcao = int(input("\t opcao: "))
    input()
    if opcao == 1:
        player1 = input("nome do player 1: ")
        player2 = input("nome do player 2: ")
        versao1(player1, player2)
    elif opcao == 2:
        player = input("nome do player: ")
        versao2(player)
    elif opcao > 2:
        print("escolha uma das opcoes!")
        input()
print("ate!")