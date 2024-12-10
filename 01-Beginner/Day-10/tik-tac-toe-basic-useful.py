import random

def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def display_board(board):
    print("---------")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("---------")

def player_move(board, symbol):
    while True:
        try:
            row, col = map(int, input("Enter your move (row and column): ").split())
            if board[row][col] == ' ':
                board[row][col] = symbol
                break
            else:
                print("The cell is already occupied! Try again.")
        except (ValueError, IndexError):
            print("Invalid input! Please enter row and column numbers between 0 and 2.")

def check_winner(board, symbol):
    # Check rows, columns, and diagonals
    for row in board:
        if all(cell == symbol for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == symbol for row in range(3)):
            return True
    if all(board[i][i] == symbol for i in range(3)) or all(board[i][2 - i] == symbol for i in range(3)):
        return True
    return False

def check_draw(board):
    return all(cell != ' ' for row in board for cell in row)

def evaluate(board):
    if check_winner(board, 'O'):
        return 10
    elif check_winner(board, 'X'):
        return -10
    else:
        return 0

def minimax(board, depth, is_maximizing):
    score = evaluate(board)

    # Terminal state
    if score == 10 or score == -10:
        return score
    if check_draw(board):
        return 0

    if is_maximizing:
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    best = max(best, minimax(board, depth + 1, not is_maximizing))
                    board[i][j] = ' '
        return best
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    best = min(best, minimax(board, depth + 1, not is_maximizing))
                    board[i][j] = ' '
        return best

def ai_move(board, symbol):
    best_val = -1000
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                move_val = minimax(board, 0, False)
                board[i][j] = ' '
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    board[best_move[0]][best_move[1]] = 'O'

def main():
    board = initialize_board()
    display_board(board)
    current_player = 'X'

    while True:
        if current_player == 'X':
            player_move(board, current_player)
        else:
            ai_move(board, current_player)

        display_board(board)

        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break
        elif check_draw(board):
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()
