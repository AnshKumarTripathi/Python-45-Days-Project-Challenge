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

import random

def ai_move(board, symbol):
    while True:
        row, col = random.randint(0, 2), random.randint(0, 2)
        if board[row][col] == ' ':
            board[row][col] = symbol
            break


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
