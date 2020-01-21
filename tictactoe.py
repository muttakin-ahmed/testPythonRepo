current_board = [['#','#','#'], ['#','#','#'], ['#','#','#']]
winner = ""

winning_combinations = {
    1: ['X','X','X'],
    2: ['O','O','O']
}

def print_board(board):
    for row in board:
        print(row)

def print_turn(player):
    print("Player" + str(player) + " plays:")
    x = int(input("Row Number:"))
    y = int(input("Column Number:"))
    play(str(player), x, y)

def play(player, x, y):
    if current_board[x][y] == '#':
        if player == '1':
            current_board[x][y] = 'X'
        else:
            current_board[x][y] = 'O'
    else:
        print("this position is already occupied, try something else!")
        print_turn(player)

def change_player(p1, p2):
    if(p1):
        p1 = False
        p2 = True
    else:
        p1 = True
        p2 = False
    return p1, p2    

def check_win():
    global winner
    for row in current_board:
        if row == winning_combinations[1] or row == winning_combinations[2]:
            print("Game Over")
            if 'X' in row:
                winner = 'X'
            else:
                winner = 'Y'
            return True
    if current_board[0][0] == current_board[1][1] == current_board[2][2] != '#':
        winner = current_board[0][0]
        return True
    elif current_board[0][2] == current_board[1][1] == current_board[2][0] != '#':
        winner = current_board[0][2]
        return True
    elif current_board[0][0] == current_board[1][0] == current_board[2][0] != '#':
        winner = current_board[0][0]
        return True
    elif current_board[0][1] == current_board[1][1] == current_board[2][1] != '#':
        winner = current_board[0][1]
        return True
    elif current_board[0][2] == current_board[1][2] == current_board[2][2] != '#':
        winner = current_board[0][2]
        return True
    print("Game is still on!!")
    return False

def check_draw():
    global drawn
    for row in current_board:
        for elem in row:
            if elem == '#':
                return False
    return True

def game():
    p1 = True
    p2 = False
    won = False
    drawn = False
    while(drawn == False and won == False):
        print_board(current_board)
        if(p1):
            print_turn(1)
        else:
            print_turn(2)
        won = check_win()
        drawn = check_draw()

        if(won == False and drawn == False):
            p1, p2 = change_player(p1, p2)
            continue
        elif won == True:
            print_board(current_board)
            print(winner + " won the game.")

        elif drawn == True:
            print_board(current_board)
            print("Match drawn.")

game()
#print(winning_combinations[1][0])
