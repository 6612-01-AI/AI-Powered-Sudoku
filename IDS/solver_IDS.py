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

def depth_limited_solve(board, depth, update_callback=None):
    if depth == 0:
        return None
    empty = find_empty(board)
    if not empty:
        return board  # Solved
    row, col = empty

    for num in range(1, 10):
        if valid(board, num, (row, col)):
            board[row][col] = num
            if update_callback:
                update_callback(board, row, col, True)
            result = depth_limited_solve(board, depth - 1, update_callback)
            if result:
                return result
            board[row][col] = 0
            if update_callback:
                update_callback(board, row, col, False)

    return None

def iterative_deepening_solve(board, update_callback=None):
    depth = 81
    while True:
        result = depth_limited_solve(board.copy(), depth, update_callback)
        if result is not None:
            return result
        depth += 1