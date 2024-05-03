import time
from collections import deque

def valid(board, num, pos):
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

def solve_bfs(initial_board):
    queue = deque([(initial_board, find_empty(initial_board))])
    start_time = time.time()
    recursion_counter = 0  # To count the number of iterations

    while queue:
        current_board, empty = queue.popleft()
        if not empty:
            end_time = time.time()
            print('Total Recursions:', recursion_counter)
            print('Time taken to solve: {:.2f} seconds'.format(end_time - start_time))
            with open("sudoku_solver_output.txt", "a") as file:
                file.write(f'Total iterations: {recursion_counter}\n')
                file.write(f'Time taken to solve: {end_time - start_time:.2f} seconds\n')
            return current_board  # Puzzle solved

        row, col = empty
        for num in range(1, 10):
            if valid(current_board, num, (row, col)):
                new_board = [row[:] for row in current_board]  # Create a new board for each possibility
                new_board[row][col] = num  # Place the number
                next_empty = find_empty(new_board)
                queue.append((new_board, next_empty))
                recursion_counter += 1

    return None