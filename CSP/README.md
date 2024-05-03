# SUDOKU solved by CSP 

### Imports
- `pygame` : A library for creating games and multimedia applications.
- `time` : Provides various time-related functions.
- `random` : Allows generation of random numbers.
- `solver_CSP` : Contains functions for solving Sudoku puzzles.

### Function Definitions
- `generate_puzzle(difficulty)` : Generates a random Sudoku puzzle based on the specified difficulty level.
- `find_empty(bo)` : Finds an empty cell in the Sudoku board.
- `redraw_window(win, board, time, strikes)` : Redraws the game window with updated information such as time and strikes.
- `format_time(secs)` : Formats the time in seconds into a readable format.
- `main()` : The main function that initializes the game window, handles user input, and runs the game loop.

### Classes
- `Cube` : Represents a single cell in the Sudoku grid. It contains methods for drawing the cell and setting its value.
- `Grid` : Represents the entire Sudoku grid. It contains methods for updating the grid, placing numbers, drawing the grid, and solving the puzzle.
