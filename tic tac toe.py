board = [' '] * 9

def print_board():
    print("\n")
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("--+---+--")

def check_winner(p):
    wins = [(0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)]
    return any(board[a] == board[b] == board[c] == p for a,b,c in wins)

player = 'X'
for turn in range(9):
    print_board()
    move = int(input(f"Player {player}, choose (1-9): ")) - 1
    if board[move] != ' ':
        print("Cell taken, try again.")
        continue
    board[move] = player
    if check_winner(player):
        print_board()
        print(f"Player {player} wins!")
        break
    player = 'O' if player == 'X' else 'X'
else:
    print_board()
    print("It's a draw!")
