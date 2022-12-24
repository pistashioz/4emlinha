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
    

def lancePx(turno, game, col, simb):
        s=0
        while win == False:
            for i in range(size[0]-1,-1,-1):
                if game[i][col-1]=='O':
                    game[i][col-1]=simb
                    break
                else:
                    s+=1
            if s==6:
                print("Coluna cheia, tente outra!")
    

def statusGame(game, win):

    #Verificar na horizontal
    for i in range(size[0]):
        winp1=0
        winp2=0
        for j in range(size[1]):
            if game[i][j]==simb:
                winp1+=1
            elif game[i][j]==simb:
                winp2+=1
        if winp1>=4:
            win=True
            print(namePlayer1, " ganhou")
        elif winp2>=4:
            win=True
            print(namePlayer2, " ganhou")
        while win == False:
            lancePx(turno, game, col, simb)
    #Verificar na vertical
    for i in range(size[1]):
        winp1 = 0
        winp2 = 0
        for j in range(size[0]):
            if game[j][i]==simb:
                winp1+=1
            elif game[j][i]==simb:
                winp2+=1
        if winp1>=4:
            win=True
            print(namePlayer1, " ganhou")
        elif winp2>=4:
            win=True
            print(namePlayer2, " ganhou")

    #Verificar na diagonal
    """
    for i in range(size[0]):
        for i in range(size[1]):
            winp1 = 0
            winp2 = 0
            for j in range(size[0]):
                for j in range(size[1]):
                    if game[j-1][i+1]==simbPlayer1:
                        winp1+=1
                    elif game[j-1][i+1]==simbPlayer2:
                        winp2+=1 
                    elif game[j+1][i+1]==simbPlayer2:
                        winp2+=1
                    elif game[j+1][i+1]==simbPlayer1:
                        winp1+=1
            if winp1>=4:
                win=True
                print(namePlayer1, " ganhou")
            elif winp2>=4:
                win=True
                print(namePlayer2, " ganhou")
   """
    while winp1 <4 or winp2 < 4:
        print(turno, end="")
        posicao = int(input(" indique a posicao para o seu simbolo: "))
        if turno == namePlayer1:
            lancePx(game,posicao,simb)
            printGame(game)
        else:
            lancePx(game,posicao,simb)
            printGame(game)
        statusGame(game,win)

namePlayer1 = input("Nome do jogador nº1: ")
simbPlayer1 = input("Digite o seu simbolo: ")
namePlayer2 = input("Nome do jogador nº2: ")
simbPlayer2 = input("Digite o seu simbolo: ")
size=[6,7]
win=False
player = [namePlayer1, namePlayer2]
turno =  random.choice(player)
if turno == namePlayer1:
    simb = simbPlayer1
    turno = namePlayer1
else:
    simb = simbPlayer2
    turno = namePlayer2

print(turno, end="")
col = int(input(" indique a posicao para o seu simbolo: "))

game = initMatriz(size)
lancePx(turno, game, col, simb)
statusGame(game, win)
printGame(game)