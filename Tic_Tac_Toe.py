import random
board=[' ' for x in range(10)]
def insertLetter(letter,pos):
    board[pos]=letter
def spaceFree(pos):
    return board[pos]==' '
def printBoard(board):
    print('  |   |')
    print(board[1]+' | '+board[2]+' | '+board[3])
    print('  |   |')
    print('-'*11)
    print('  |   |')
    print(board[4]+' | '+board[5]+' | '+board[6])
    print('  |   |')
    print('-'*11)
    print('  |   |')
    print(board[7]+' | '+board[8]+' | '+board[9])
    print('  |   |')
def isWinner(bo,le):
    for i in range(1,10,3):
        if bo[i]==le and bo[i+1]==le and bo[i+2]==le:
            return True
    for i in range(1,4):
        if bo[i]==le and bo[i+3]==le and bo[i+6]:
            return True
    if bo[1]==le and bo[5]==le and bo[9]==le:
        return True
    if bo[3]==le and bo[5]==le and bo[7]==le:
        return True
    return False
def playerMove():
    run=True
    while run:
        move=input("please select a position to place \'x\' (1-9): ")
        try:
            move=int(move)
            if move>0 and move<10:
                if spaceFree(move):
                    run=False
                    insertLetter('X',move)
                else:
                    print("sorry, this place is occupied!")
            else:
                print("please type a number within the range!")
        except:
            print("please type a number")
def compMove():
    possible_moves=[x for x,letter in enumerate(board) if letter ==' ' and x!=0]
    move=0
    for let in ['O','X']:
        for i in possible_moves:
            boardCopy=board[:]
            boardCopy[i]=let
            if isWinner(boardCopy,let):
                move=i
                return move
    cornerOpen=[]
    for i in possible_moves:
        if i in [1,3,7,9]:
            cornerOpen.append(i)
    if len(cornerOpen)>0:
        move=selectRandom(cornerOpen)
        return move
    if 5 in possible_moves:
        move=5
        return move
    edgesOpen=[]
    for i in possible_moves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
    if len(edgesOpen)>0:
        move=selectRandom(edgesOpen)
    return move
    
    
def selectRandom(li):
    import random
    ln=len(li)
    r=random.randrange(0,ln)
    return li[r]
def isboardFull(board):
    if board.count(' ')>1:
        return False
    return True
def main():
    print("Welcome to Tic Tac Toe")
    printBoard(board)
    while not(isboardFull(board)):
        if not(isWinner(board,'O')):
            playerMove()
            printBoard(board)
            print()
        else:
            print('sorry, O\'s won this time!')
            break
        if not(isWinner(board,'X')):
            move=compMove()
            if move==0:
                print("Tie Game!")
            else:
                insertLetter('O',move)
                print('Computer placed an \'O\' in position',move)
                printBoard(board)
        else:
            print('X\'s won this time! Good Job!')
            break
    if isboardFull(board):
        print("Tie Game!")
main()
               
    


