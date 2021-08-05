board = [[' ' for i in range(3)] for j in range(3)]

# board[1][2] = 'X'
# board[0][1] = 'O'


def display():
    for i in range(3):
        print("+---" * 3 + '+')
        for j in range(3):
            print(f"| {board[i][j]} ", end='')
        print('|')
    print("+---" * 3 + '+')


def is_win(player):
    win1 = True
    win2 = True
    for i in range(3):
        win1 = win1 and board[i][i] == player
        win2 = win2 and board[i][2 - i] == player
        win_ij = True
        win_ji = True
        # win = board[i][0] == player and board[i][1] == player and board[i][2] == player
        for j in range(3):
            win_ij = win_ij and board[i][j] == player
            win_ji = win_ji and board[j][i] == player
        if win_ij or win_ji:
            return True
    if win1 or win2:
        return True
    return False


moves = ['X', 'O']
current_move = 0
cnt = 0
while True:
    display()
    print(f"{moves[current_move]} is moving")
    x, y = map(int, input().split())
    if x > 2 or x < 0 or y > 2 or y < 0:
        print("No such coordinate. Try again.")
    elif board[x][y] != ' ':
        print("Cell is occupied. Try again.")
    else:
        cnt += 1
        board[x][y] = moves[current_move]
        if is_win(moves[current_move]):
            display()
            print(f"Player {moves[current_move]} win!")
            break
        elif cnt == 9:
            display()
            print("Game over. Draw.")
            break
        current_move = (current_move + 1) % 2