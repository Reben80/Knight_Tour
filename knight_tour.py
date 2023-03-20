import pygame
import numpy as np


# The previous code for finding the Knight's Tour using Warnsdorf's rule

# Add the find_knights_tour function and other necessary functions here


def is_valid_move(board, x, y):
    return 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == -1


def count_valid_moves(board, x, y):
    moves = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]

    count = 0
    for move in moves:
        new_x, new_y = x + move[0], y + move[1]
        if is_valid_move(board, new_x, new_y):
            count += 1
    return count


def knights_tour(board, x, y, move_count):
    if move_count == len(board) * len(board[0]):
        return True

    moves = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]

    next_moves = [(move, count_valid_moves(board, x + move[0], y + move[1])) for move in moves]
    next_moves = sorted(next_moves, key=lambda x: x[1])

    for move, _ in next_moves:
        new_x, new_y = x + move[0], y + move[1]

        if is_valid_move(board, new_x, new_y):
            board[new_x][new_y] = move_count
            if knights_tour(board, new_x, new_y, move_count + 1):
                return True
            board[new_x][new_y] = -1

    return False


def find_knights_tour(board_size):
    board = np.full((board_size, board_size), -1)

    board[0][0] = 0
    if knights_tour(board, 0, 0, 1):
        return board
    else:
        return None


board_size = 10
result = find_knights_tour(board_size)
if result is not None:
    print("Knight's Tour found:")
    print(result)
else:
    print("No Knight's Tour found.")

def draw_board(screen, board, cell_size):
    colors = [(255, 255, 255), (153, 153, 153)]
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            color = colors[(i + j) % 2]
            pygame.draw.rect(screen, color, pygame.Rect(j * cell_size, i * cell_size, cell_size, cell_size))

    moves = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]

    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            move_number = board[i, j]
            if move_number != -1:
                for move in moves:
                    new_i, new_j = i + move[0], j + move[1]
                    if 0 <= new_i < board.shape[0] and 0 <= new_j < board.shape[1] and board[
                        new_i, new_j] == move_number + 1:
                        start_pos = (j * cell_size + cell_size // 2, i * cell_size + cell_size // 2)
                        end_pos = (new_j * cell_size + cell_size // 2, new_i * cell_size + cell_size // 2)
                        pygame.draw.line(screen, (0, 0, 0), start_pos, end_pos, 2)
                        break


def main():
    board_size = 10
    cell_size = 80
    result = find_knights_tour(board_size)

    if result is not None:
        pygame.init()
        screen = pygame.display.set_mode((board_size * cell_size, board_size * cell_size))
        pygame.display.set_caption("Knight's Tour")

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            draw_board(screen, result, cell_size)
            pygame.display.flip()

        pygame.quit()
    else:
        print("No Knight's Tour found.")


if __name__ == "__main__":
    main()