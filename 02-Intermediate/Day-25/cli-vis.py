board = [' ' for _ in range(9)]

def print_board(board):
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("--+---+--")

def check_winner(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def check_draw(board):
    return all(cell != ' ' for cell in board)

move_counter = {}

def minimax(board, is_maximizing, depth=0):
    global move_counter
    if depth not in move_counter:
        move_counter[depth] = 0

    if check_winner(board, 'O'):
        return 1  # AI wins
    elif check_winner(board, 'X'):
        return -1  # Player wins
    elif check_draw(board):
        return 0  # Draw

    best_score = -float('inf') if is_maximizing else float('inf')
    for i in range(9):
        if board[i] == ' ':
            move_counter[depth] += 1
            board[i] = 'O' if is_maximizing else 'X'
            print(f"Evaluating move at depth {depth}:")
            print_board(board)
            score = minimax(board, not is_maximizing, depth + 1)
            board[i] = ' '
            best_score = max(score, best_score) if is_maximizing else min(score, best_score)
    return best_score

def best_move(board):
    best_score = -float('inf')
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

def print_move_counter():
    print("\nNumber of possible moves at each depth:")
    for depth in sorted(move_counter):
        print(f"Depth {depth}: {move_counter[depth]} possible moves")

def main():
    global board
    player = 'X'
    while True:
        print_board(board)
        if player == 'X':
            move = int(input("Enter your move (1-9): ")) - 1
        else:
            move = best_move(board)
        if board[move] == ' ':
            board[move] = player
            if check_winner(board, player):
                print_board(board)
                print(f"{player} wins!")
                break
            elif check_draw(board):
                print_board(board)
                print("It's a draw!")
                break
            player = 'O' if player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")
    
    print_move_counter()

if __name__ == "__main__":
    main()
