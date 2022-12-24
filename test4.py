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
    while win == False:
        for i in range(size[0]-1,-1,-1):
            if game[i][col-1]=='O':
                game[i][col-1]=simb
                break
            else:
                s+=1
        if s==6:
            print("Coluna cheia, tente outra!")

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
        #na vertical

    #for i in range(size[1]):
       # for j in range(size[0]):
            




size=[6,7]

namePlayer1 = input("Nome do jogador nº1: ")
simbPlayer1 = input("Digite o seu simbolo: ")
namePlayer2 = input("Nome do jogador nº2: ")
simbPlayer2 = input("Digite o seu simbolo: ")
win=False
player = [namePlayer1, namePlayer2]
turno =  random.choice(player)
if turno == namePlayer1:
    simb = simbPlayer1
    turno = namePlayer1
else:
    simb = simbPlayer2
    turno = namePlayer2

game = initMatriz(size)
printGame(game)
print(turno, end="")
col = int(input(" indique a posicao para o seu simbolo: "))
lancePx(game,col,simb)
statusGame(game,win)
printGame(game)

size=[6,7]