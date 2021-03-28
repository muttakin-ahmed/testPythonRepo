def numRookCaptures(board):
    count = 0
    rx = 0
    ry = 0
    for i in range(len(board)):
        if "R" in board[i]:
            rx = i
            ry = board[i].index("R")
            break
    
    #right move
    for i in range(rx+1, 8):
        if board[i][ry] == "B":
            break
        if board[i][ry] == "p":
            count += 1
            break
        
    #left move
    for i in range(0, rx-1):
        if board[i][ry] == "B":
            break
        if board[i][ry] == "p":
            count += 1
            break
        
    #down move
    for i in range(ry+1, 8):
        if board[rx][i] == "B":
            break
        if board[rx][i] == "p":
            count += 1
            break
        
    #up move
    for i in range(0, ry-1):
        if board[i][ry] == "B":
            break
        if board[i][ry] == "p":
            count += 1
            break
        
    return count
    d = [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
    print(numRookCaptures(d))
