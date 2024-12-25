import pygame
import sys

# Constants
MAIN_WIDTH, MAIN_HEIGHT = 600, 200  # Main game size
TREE_WIDTH, TREE_HEIGHT = 1200, 600  # Tree visualization size
SQUARE_SIZE = MAIN_WIDTH // 3  # Square size for main game
MINI_SQUARE_SIZE = TREE_WIDTH // 9  # Square size for mini boards
LINE_WIDTH = 5
CIRCLE_RADIUS = SQUARE_SIZE // 4
MINI_CIRCLE_RADIUS = MINI_SQUARE_SIZE // 4
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4
MINI_SPACE = MINI_SQUARE_SIZE // 4
BORDER_COLOR = (255, 255, 255)  # White color for borders

# Colors
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (84, 84, 84)

# Initialize Pygame
pygame.init()
main_screen = pygame.display.set_mode((MAIN_WIDTH, MAIN_HEIGHT))
tree_screen = pygame.display.set_mode((TREE_WIDTH, TREE_HEIGHT))
pygame.display.set_caption('Tic Tac Toe AI Visualization')
main_screen.fill(BG_COLOR)
tree_screen.fill(BG_COLOR)

def draw_main_lines():
    for row in range(1, 3):
        pygame.draw.line(main_screen, LINE_COLOR, (0, row * SQUARE_SIZE), (MAIN_WIDTH, row * SQUARE_SIZE), LINE_WIDTH)
    for col in range(1, 3):
        pygame.draw.line(main_screen, LINE_COLOR, (col * SQUARE_SIZE, 0), (col * SQUARE_SIZE, MAIN_HEIGHT), LINE_WIDTH)

def draw_tree_lines():
    for row in range(6):
        for col in range(9):
            start_x = col * MINI_SQUARE_SIZE
            start_y = row * MINI_SQUARE_SIZE
            pygame.draw.rect(tree_screen, BORDER_COLOR, (start_x, start_y, MINI_SQUARE_SIZE, MINI_SQUARE_SIZE), LINE_WIDTH)
            pygame.draw.line(tree_screen, LINE_COLOR, (start_x, start_y + MINI_SQUARE_SIZE // 3), (start_x + MINI_SQUARE_SIZE, start_y + MINI_SQUARE_SIZE // 3), LINE_WIDTH)
            pygame.draw.line(tree_screen, LINE_COLOR, (start_x, start_y + 2 * MINI_SQUARE_SIZE // 3), (start_x + MINI_SQUARE_SIZE, start_y + 2 * MINI_SQUARE_SIZE // 3), LINE_WIDTH)
            pygame.draw.line(tree_screen, LINE_COLOR, (start_x + MINI_SQUARE_SIZE // 3, start_y), (start_x + MINI_SQUARE_SIZE // 3, start_y + MINI_SQUARE_SIZE), LINE_WIDTH)
            pygame.draw.line(tree_screen, LINE_COLOR, (start_x + 2 * MINI_SQUARE_SIZE // 3, start_y), (start_x + 2 * MINI_SQUARE_SIZE // 3, start_y + MINI_SQUARE_SIZE), LINE_WIDTH)

def draw_main_figures(board):
    for row in range(3):
        for col in range(3):
            if board[row * 3 + col] == 'X':
                pygame.draw.line(main_screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)
                pygame.draw.line(main_screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
            elif board[row * 3 + col] == 'O':
                pygame.draw.circle(main_screen, CIRCLE_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), CIRCLE_RADIUS, CIRCLE_WIDTH)

def draw_tree_figures(board, offset_x=0, offset_y=0):
    for row in range(3):
        for col in range(3):
            if board[row * 3 + col] == 'X':
                pygame.draw.line(tree_screen, CROSS_COLOR, (col * MINI_SQUARE_SIZE + MINI_SPACE + offset_x, row * MINI_SQUARE_SIZE + MINI_SPACE + offset_y),
                                 (col * MINI_SQUARE_SIZE + MINI_SQUARE_SIZE - MINI_SPACE + offset_x, row * MINI_SQUARE_SIZE + MINI_SQUARE_SIZE - MINI_SPACE + offset_y), CROSS_WIDTH)
                pygame.draw.line(tree_screen, CROSS_COLOR, (col * MINI_SQUARE_SIZE + MINI_SPACE + offset_x, row * MINI_SQUARE_SIZE + MINI_SQUARE_SIZE - MINI_SPACE + offset_y),
                                 (col * MINI_SQUARE_SIZE + MINI_SQUARE_SIZE - MINI_SPACE + offset_x, row * MINI_SQUARE_SIZE + MINI_SPACE + offset_y), CROSS_WIDTH)
            elif board[row * 3 + col] == 'O':
                pygame.draw.circle(tree_screen, CIRCLE_COLOR, (int(col * MINI_SQUARE_SIZE + MINI_SQUARE_SIZE // 2 + offset_x), int(row * MINI_SQUARE_SIZE + MINI_SQUARE_SIZE // 2 + offset_y)), MINI_CIRCLE_RADIUS, CIRCLE_WIDTH)

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

def minimax(board, is_maximizing, depth=0, offset_x=0, offset_y=0):
    if check_winner(board, 'O'):
        return 1  # AI wins
    elif check_winner(board, 'X'):
        return -1  # Player wins
    elif check_draw(board):
        return 0  # Draw

    best_score = -float('inf') if is_maximizing else float('inf')
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O' if is_maximizing else 'X'
            draw_tree_figures(board, offset_x, offset_y)
            pygame.display.update()
            pygame.time.wait(300)
            score = minimax(board, not is_maximizing, depth + 1, offset_x + (depth % 9) * MINI_SQUARE_SIZE * 3, offset_y + (depth // 9) * MINI_SQUARE_SIZE * 3)
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

def main():
    global board
    board = [' ' for _ in range(9)]
    draw_main_lines()
    draw_tree_lines()
    player = 'X'
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if player == 'X':
                    mouseX = event.pos[0]  # x-coordinate
                    mouseY = event.pos[1]  # y-coordinate

                    clicked_row = mouseY // SQUARE_SIZE
                    clicked_col = mouseX // SQUARE_SIZE

                    index = clicked_row * 3 + clicked_col

                    if board[index] == ' ':
                        board[index] = player
                        draw_main_figures(board)
                        if check_winner(board, player):
                            print(f"{player} wins!")
                            pygame.quit()
                            sys.exit()
                        elif check_draw(board):
                            print("It's a draw!")
                            pygame.quit()
                            sys.exit()
                        player = 'O'
            
            if player == 'O':
                move = best_move(board)
                if board[move] == ' ':
                    board[move] = player
                    draw_main_figures(board)
                    if check_winner(board, player):
                        print(f"{player} wins!")
                        pygame.quit()
                        sys.exit()
                    elif check_draw(board):
                        print("It's a draw!")
                        pygame.quit()
                        sys.exit()
                    player = 'X'

        pygame.display.update()

if __name__ == "__main__":
    main()
