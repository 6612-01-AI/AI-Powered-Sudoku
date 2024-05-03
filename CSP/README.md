# SUDOKU solved by CSP 

## Introduction 
Welcome to the Sudoku Solver project! This Python-based application utilizes the Pygame library to create an interactive graphical user interface (GUI) for solving Sudoku puzzles. Whether you're a Sudoku enthusiast looking to sharpen your skills or simply seeking a fun way to pass the time, this solver offers both manual puzzle-solving and automated solving capabilities.

The solver employs a combination of backtracking algorithms and constraint satisfaction techniques to efficiently find solutions to Sudoku puzzles. By generating random Sudoku puzzles of varying difficulties and providing intuitive input controls, users can enjoy a personalized Sudoku-solving experience tailored to their preferences and skill level.

## Key Features:
1. **Interactive GUI**: The Pygame-based GUI allows users to interact with the Sudoku grid using mouse clicks and keyboard inputs, providing a seamless and intuitive solving experience.
2. **Random Puzzle Generation**: The solver generates random Sudoku puzzles of adjustable difficulty levels, ensuring endless gameplay possibilities for users.
3. **Manual and Automated Solving**: Users can manually input numbers into the grid or opt for automated solving using the built-in solver algorithms.
4. **Constraint Satisfaction Techniques**: The solver employs constraint satisfaction techniques such as forward checking and backtracking to efficiently find solutions to Sudoku puzzles while ensuring all constraints are satisfied.
5. **Performance Metrics**: The solver tracks and records performance metrics such as the total number of recursive calls and the time taken to solve each puzzle, providing insights into the efficiency of the solving algorithms.

### Imports
- `pygame` : A library for creating games and multimedia applications.
- `time` : Provides various time-related functions.
- `random` : Allows generation of random numbers.
- `solver_CSP` : Contains functions for solving Sudoku puzzles.

  ```
  pip install pygame
  ```

  ```
  import pygame
  import time
  import random
  from solver_CSP import solve, valid

  ```

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
