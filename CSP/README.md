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

## Explanation:
- The ```generate_puzzle``` function creates a random Sudoku puzzle based on the specified difficulty level.
- The ```Cube``` class represents a single cell in the Sudoku grid. It handles drawing the cell and setting its value.
- The ```Grid``` class represents the entire Sudoku grid. It contains a 2D array of ```Cube``` objects and methods for updating the grid, placing numbers, drawing the grid, and solving the puzzle.
- The ```main``` function initializes the game window, creates a Sudoku grid, and runs the game loop. It handles user input for entering numbers, clearing cells, and solving the puzzle.
