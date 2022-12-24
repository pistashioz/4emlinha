#import os
import random
def initMatriz(size):

    m = [['O' for j in range (size[1])] for i in range(size[0])]
    return m

def printGame(game):
    print("\t\t\t------------Jogo 4 em linha---------")
    print("\t\t\t --1----2----3----4----5----6----7--\n")
    for i in range(size[0]):
        print('\t\t\t',game[i])

    print()

def lancePx(game,col,simb):
    s=0
    for i in range(size[0]-1,-1,-1):
        if game[i][col-1]=='O':
            game[i][col-1]=simb
            break
        else:
            s+=1
    if s==6:
        print("Coluna cheia, tente outra!")
        
def versao1(game): #hacer un fow loop o un while hasta que alguien gane salga 
    player = [namePlayer1, namePlayer2]
    turno =  random.choice(player)
    return statusGame(game,win)
    while winp1 <4 or winp2 < 4:
        print(turno, end="")
        posicao = int(input(" indique a posicao para o seu simbolo: "))
        if turno == namePlayer1:
            lancePx(game,posicao,'P')
            printGame(game)
        else:
            lancePx(game,posicao,'X')
            printGame(game)
        statusGame(game,win)


def statusGame(game,win):

    
    #Verificar na horizontal
    
    for i in range(size[0]):

        winp1=0
        winp2=0
        for j in range(size[1]):
            if game[i][j]==simbPlayer1:
                winp1+=1
            elif game[i][j]==simbPlayer2:
                winp2+=1
        if winp1>=4:
            win=True
            print("jogador 1 ganhou")
        elif winp2>=4:
            win=True
            print("jogador 2 ganhou")
    #Verificar na vertical

    for i in range(size[1]):
        winp1 = 0
        winp2 = 0
        for j in range(size[0]):
            if game[j][i]==simbPlayer1:
                winp1+=1
            elif game[j][i]==simbPlayer2:
                winp2+=1
        if winp1>=4:
            win=True
            print(namePlayer1, " ganhou")
        elif winp2>=4:
            win=True
            print(namePlayer2, " ganhou")

    #verificar na diagonal!!!!
"""
    for i in range(size):
        winp1 = 0
        winp2 = 0
        for j in range(size[0]):
            if game[j+1][i+1]==simbPlayer1:
                winp1+=1
            elif game[j+1][i+1]==simbPlayer2:
                winp2+=1
            elif game[j-1][i-1]==simbPlayer2:
                winp2+=1
            elif game[j-1][i-1]==simbPlayer1:
                winp1+=1
        if winp1>=4:
            win=True
            print(namePlayer1, " ganhou")
        elif winp2>=4:
            win=True
            print(namePlayer2, " ganhou")
"""
size=[6,7]




opcao = 9
while opcao != 0:
    #os.system("cls")
    print("MENU \n 1 - Player1 vs Player2 \n 2 - Player vs computador  \n 0 - Sair")
    opcao = int(input("\t opcao: "))
    input()
    if opcao == 1:
        namePlayer1 = input("Nome do jogador nº1: ")
        simbPlayer1 = input("Digite o seu simbolo: ")
        namePlayer2 = input("Nome do jogador nº2: ")
        simbPlayer2 = input("Digite o seu simbolo: ")
        win=''
        game = initMatriz(size)
        versao1(game)

    elif opcao == 2:
        player = input("nome do player: ")
        versao2(player)
    elif opcao > 2:
        print("escolha uma das opcoes!")
        input()
print("ate!")
