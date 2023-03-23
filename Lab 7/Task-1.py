#Task5
import numpy as np

board=np.empty(shape=(3,3),dtype=str)
print("User's Character is O || Agent's Character is X")
def checkWinner():
    global board
    for i in range(3):
        if board[i][0]==board[i][1] and board[i][1]==board[i][2]:
            if board[i][0]=='X':
                return 'X'
            elif board[i][0]=='O':
                return 'O'
    for j in range(3):
        if board[0][j]==board[1][j] and board[1][j]==board[2][j]:
            if board[0][j]=='X':
                return 'X'
            elif board[0][j]=='O':
                return 'O'
            
    if board[0][0]==board[1][1] and board[1][1]==board[2][2]:
        if board[0][0]=='X':
            return 'X'
        elif board[0][0]=='O':
            return 'O'
    if board[0][2]==board[1][1] and board[1][1]==board[2][0]:
        if board[0][2]=='X':
            return 'X'
        elif board[0][2]=='O':
            return 'O'
    if len(list((space for space in np.nditer(board) if space=='')))==0:
        return 'Tie'
    else:
        return 'Continue'
        

def genScore():
    global board
    score=0
    for i in range(3):
        if board[i][0]==board[i][1] and board[i][1]==board[i][2]:
            if board[i][0]=='X':
                score=10
                return score
            elif board[i][0]=='O':
                score=-10
                return score
    for j in range(3):
        if board[0][j]==board[1][j] and board[1][j]==board[2][j]:
            if board[0][j]=='X':
                score=10
                return score
            elif board[0][j]=='O':
                score=-10
                return score
            
    if board[0][0]==board[1][1] and board[1][1]==board[2][2]:
        if board[0][0]=='X':
            score=10
            return score
        elif board[0][0]=='O':
            score=-10
            return score
    if board[0][2]==board[1][1] and board[1][1]==board[2][0]:
        if board[0][2]=='X':
            score=10
            return score
        elif board[0][2]=='O':
            score=-10
            return score
        
    return score
    
    
def minimax(depth,maximize):
    global board
    score=genScore()
    
    if score==10:
        return score
    if score==-10:
        return score
    if len(list((space for space in np.nditer(board) if space=='')))==0:
        return 0
    if maximize:
        bestVal=-1000
        for i in range(3):
            for j in range(3):
                if board[i][j]=='':
                    board[i][j]='X'
                    bestVal=max(bestVal,minimax(depth+1,not maximize))
                    board[i][j]=''
        return bestVal
    else:
        bestVal=1000
        for i in range(3):
            for j in range(3):
                if board[i][j]=='':
                    board[i][j]='O'
                    bestVal=min(bestVal,minimax(depth+1,not maximize))
                    board[i][j]=''
        return bestVal
        
def makeMove():
    global board
    bestVal=-1000
    move=(-1,-1)
    for i in range(3):
        for j in range(3):
            if board[i][j]=='':
                board[i][j]='X'
                currVal=minimax(0,False)
                board[i][j]=''
                if bestVal<currVal:
                    bestVal=currVal
                    move=(i,j)
    board[move[0],move[1]]='X'
                
            
    
count=0 
while True:
    index=int(input("Enter your move (1-9): "))
    row=int((index-1)/3)
    col=(index-1)%3
    if board[row][col]!='':
        print('Wrong move! Please try again with a valid move.')
        continue
    board[row][col]='O'
    if checkWinner()=='O':
        print(board,'\n')
        print('O Wins')
        break
    makeMove()
    if checkWinner()=='X':
        print(board,'\n')
        print('X Wins')
        break
    elif checkWinner()=='Tie':
        print(board,'\n')
        print('Tie Game')
        break
    print(board,'\n')