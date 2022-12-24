#Victoria Martinez N° 40220096
import os
def initMatriz(size): #funcao que cria o tabuleiro do nosso jogo

    m = [['0' for j in range (size[1])] for i in range(size[0])]
    return m

def printGame(game):
    print("-----------------Jogo 4 em linha------------------")
    print("-1------2-------3-------4-------5-------6-------7-\n")
    for i in range(size[0]):
        for j in range(size[1]):
            print(game[i][j], end="\t")
        print("\n")

    print()

def lance(player, game, simb):
    s=0
    print(players, end="")
    col = int(input(" indique a posicao para o seu simbolo: "))
    
    if col <= 0 or col > 7:
        print("coluna nao valida, tente outra!")
        lance(player, game, simb)
    else: 
        if players == namePlayer1:
            for i in range(size[0]-1,-1,-1): #aqui fazemos uma substituicao: se a matriz se encontra vazia (ou seja, tem um 0) essa posicao vai ser ocupada pelo simbolo
                if game[i][col-1]=='0':
                    game[i][col-1]=simbPlayer1
                    os.system("cls")
                    break
                else:
                    s+=1 #o simbolo do jogador vai ir a mesma coluna mas em cima do simbolo que se encontrava nesta coluna previamente
            if s==6:
                print("Coluna cheia, tente outra!")
                lance(player, game, simb)
                input()
        elif players == namePlayer2:
            for i in range(size[0]-1,-1,-1):
                if game[i][col-1]=='0':
                    game[i][col-1]=simbPlayer2
                    os.system("cls")
                    break
                else:
                    s+=1
            if s==6:
                print("Coluna cheia, tente outra!")
                lance(player, game, simb)

def statusGame(game,win):
    #Verificar na vertical
    
    for i in range(size[1]):
        lista1 =[]

        for j in range(size[0]):
            lista1.append(game[j][i])
        if ''.join(lista1).__contains__(simbPlayer1*4):
            print(namePlayer1, " ganhou")
            return True
        elif ''.join(lista1).__contains__(simbPlayer2*4):
            print(namePlayer2, " ganhou")
            return True

    #Verificar na horizontal
    for i in range(size[0]):
        s1 = ''.join(game[i])
        for j in range(size[1]):
            if s1.__contains__(simbPlayer1*4):
                print(namePlayer1, " ganhou")
                return True
            elif s1.__contains__(simbPlayer2*4):
                print(namePlayer2, " ganhou")
                return True

    #Verificar na diagonal
    for i in range(size[0] - 3): #verifica desde a ponta da direita ate o final da esquerda na diagonal (/)
        os.system("cls")
        for j in range(3, size[1]):
            if game[i][j] == simbPlayer1 and game[i+1][j-1] == simbPlayer1 and game[i+2][j-2] == simbPlayer1 and game[i+3][j-3] == simbPlayer1:
                print(namePlayer1, " ganhou")
                printGame(game)
                return True

            elif game[i][j] == simbPlayer2 and game[i+1][j-1] == simbPlayer2 and game[i+2][j-2] == simbPlayer2 and game[i+3][j-3] == simbPlayer2:
                print(namePlayer2, " ganhou")
                printGame(game)
                return True

    
    for i in range(size[0] - 3): #verifica desde a ponta da esquerda ate o final da direita na diagonal (\)
        for j in range(size[1] - 3):
            if game[i][j] == simbPlayer1 and game[i+1][j+1] == simbPlayer1 and game[i+2][j+2] == simbPlayer1 and game[i+3][j+3] == simbPlayer1:
                printGame(game)
                print(namePlayer1, " ganhou")
                return True
            elif game[i][j] == simbPlayer2 and game[i+1][j+1] == simbPlayer2 and game[i+2][j+2] == simbPlayer2 and game[i+3][j+3] == simbPlayer2:
                printGame(game)
                print(namePlayer2, " ganhou")
                return True
    




size=[6,7]
opcao = 9
simb = []
player = []
win=False
while opcao != 0:
    os.system("cls")
    print("\t\tMENU")
    print("1 - Player1 vs Plaver2")
    print("0 - Sair")
    opcao = int(input("Escolha uma das opções: "))
    if opcao == 1:
        namePlayer1 = input("Nome do jogador nº1: ")
        namePlayer2 = input("Nome do jogador nº2: ")
        player.append(namePlayer1)
        player.append(namePlayer2)
        simbPlayer1 = "🔴" #input("Digite o seu simbolo: ")
        simbPlayer2 = "🔵" #input("Digite o seu simbolo: ")
        simb.append(simbPlayer1)
        simb.append(simbPlayer2)
        game = initMatriz(size)
        while win != True:
            for players in player:
                printGame(game)
                lance(player, game, simb)
                printGame(game)
                win =statusGame(game,win)
                if win==True:
                    break
        newGame = input("quer jogar de novo? (S/N)")
        if newGame.upper()=='N':
            opcao=0
        elif newGame.upper()=='S':
            opcao=9
            player.clear()
            win = newGame
print("\n\nObrigado, volte sempre! :-) ")


