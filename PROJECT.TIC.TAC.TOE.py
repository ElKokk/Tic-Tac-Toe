def DisplayBoard(board):
    if board==[[1,2,3],[4,5,6],[7,8,9]]:

        print("The game is about to begin..."," \n ")
        print("Computer plays first:","\n ")
        board[1][1]="X"
    print("+-------+-------+-------+\n|       |       |       |\n|  ",board[0][0],"  |  ",board[0][1],"  |  ",board[0][2],"  |\n|       |       |       |\n+-------+-------+-------+\n|       |       |       |\n|  ",board[1][0],"  |  ",board[1][1],"  |  ",board[1][2],"  |\n|       |       |       |\n+-------+-------+-------+\n|       |       |       |\n|  ",board[2][0],"  |  ",board[2][1],"  |  ",board[2][2],"  |\n|       |       |       |\n+-------+-------+-------+\n")

def EnterMove(board):
    while True:
        try:
            UserMove=int(input("Make your move:" ))
            if UserMove<1 or UserMove>9:
                print("Play to a valid position, between 1 and 9")
                continue
        except:
            print("Enter an integer number between 1 and 9")
            continue
        check=None
        for i in range(0,3):
            for j in range(0,3):
                if board[i][j]==UserMove:
                    board[i][j]="O"
                    check=True
                    break
            if check==True:
                break
        if check!=True:
            print("This position is already taken, pick another position")
            continue
        else:
            break
    return board

def MakeListOfFreeFields(board):
    Moves=["X","O"]
    global FreeSquares
    FreeSquares=[]
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] not in Moves:
                tup=(i,j)
                FreeSquares.append(tup)
    return FreeSquares


def VictoryFor(board, sign):
    if board[0][0]==board[1][1]==board[2][2]=="O" or board[0][2]==board[1][1]==board[2][0]=="O":
            print("You won!")
            sign=True
            return sign
    if board[0][0]==board[1][1]==board[2][2]=="X" or board[0][2]==board[1][1]==board[2][0]=="X":
            print("You lost, Computer wins!")
            sign=True
            return sign
    for i in range(0,3):
        if board[i][0]==board[i][1]==board[i][2]=="O" or board[0][i]==board[1][i]==board[2][i]=="O":
            print("You won!")
            sign=True
            break
        elif board[i][0]==board[i][1]==board[i][2]=="X" or board[0][i]==board[1][i]==board[2][i]=="X":
            print("You lost, Computer wins!")
            sign=True
            break
        elif len(FreeSquares)<1:
            print("It's a tie!")
            sign=True
            break
    return sign

def DrawMove(board):
    from random import randrange
    free=[]
    for i in FreeSquares:
        free.append(board[i[0]][i[1]])
    while True:
        ComputerMove=randrange(1,10)
        if ComputerMove not in free:
            continue
        else:
            for i in FreeSquares:
                if board[i[0]][i[1]]==ComputerMove:
                    board[i[0]][i[1]]="X"
                    return board

board=[[1,2,3],[4,5,6],[7,8,9]]
DisplayBoard(board)
sign=None
while True:
    EnterMove(board)
    DisplayBoard(board)
    MakeListOfFreeFields(board)
    if VictoryFor(board,sign):
        break

    DrawMove(board)
    DisplayBoard(board)
    MakeListOfFreeFields(board)
    if VictoryFor(board,sign):
        break
print("Thank you for playing")
