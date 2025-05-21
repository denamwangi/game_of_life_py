import os
import time

# RULES:
# Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overpopulation.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

def print_board(board):
    for row in board:
        print("\n ")
        for val in row:
            if val == True:
                print('🐙', end=" ")
            else:
                print(".", end="  ")
    print("\n ")



def instantiate():
    board = [[False for i in range(16)] for i in range(16)]
    board[7][8] = True
    board[8][8] = True
    board[8][9] = True
    board[8][10] = True
    board[6][9] = True
    return board

def count_live_neighbors(row, col, board_size):
    neighbor_count = 0
    for diff_index in [[0, 1], [0, -1], [1, 1], [-1, -1], [-1, 0], [1, 0], [-1, 1], [1, -1]]:
        new_row, new_col = row + diff_index[0], col + diff_index[1]
        if new_row < 0: 
            new_row = board_size - 1
        if new_col < 0:
            new_col = board_size - 1
        if new_col == board_size:
            new_col = 0
        if new_row == board_size:
            new_row = 0
        if board[new_row][new_col] == True:
            neighbor_count += 1
    
    return neighbor_count

def run_board(board):
    next_board = [[False for i in range(len(board))] for i in range(len(board))]

    for row_index, row in enumerate(board):
        for col_index, val in enumerate(row):
            live_neighbors= count_live_neighbors(row_index, col_index, len(board))
            if val == True and (live_neighbors == 2 or live_neighbors == 3):
                next_board[row_index][col_index] = True
            elif val == False and live_neighbors == 3:
                next_board[row_index][col_index] = True
    print_board(next_board)
    return next_board




if __name__ == "__main__":
    initial_board = instantiate()
    board = initial_board
    while True:
        os.system('clear')
        board = run_board(board)
        time.sleep(.1)
