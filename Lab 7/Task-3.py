#n queens problem
def is_valid(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i, j = i-1, j-1
    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i, j = i+1, j-1   
    return True


def solve(board, col, n):    
    if col >= n:
        return True   
    for i in range(n):
        if is_valid(board, i, col, n):
            board[i][col] = 1     
            if solve(board, col+1, n):
                return True           
            board[i][col] = 0   
    return False


def print_solution(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            print(str(board[row][col]) +' ',end=' ')
        print()


n = int(input("Enter the number of queens: ")) 
board = [[0 for x in range(n)] for y in range(n)]    

if solve(board, 0, n):    
    print_solution(board)    
else:    
    print("No solution exists.")