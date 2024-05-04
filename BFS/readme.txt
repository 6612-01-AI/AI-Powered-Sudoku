# SUDOKU Solved by BFS
## Introduction

This Python-based application uses the Pygame library to provide an interactive graphical user interface (GUI) for solving Sudoku puzzles. It leverages the Breadth-First Search (BFS) algorithm, renowned for its systematic exploration of solutions, ensuring all possible board configurations are considered.

## Key Features:

'Interactive GUI:' Powered by Pygame, this GUI facilitates intuitive interaction with the Sudoku grid, allowing users to input numbers using mouse clicks and keyboard controls.
'Random Puzzle Generation:' Automatically generates random Sudoku puzzles across various difficulty levels, catering to different user preferences and ensuring a dynamic challenge.
'Automated Solving with BFS:' The application features automated puzzle solving using the BFS algorithm, which explores all possible moves level-by-level, ensuring comprehensive solution assessment.
'BFS Algorithm Implementation:' Implements BFS to methodically explore every potential solution, guaranteeing that the first solution found is the shortest path to the puzzle's completion.
'Performance Metrics:' Tracks performance metrics like the number of iterations and the time taken to solve puzzles, illustrating the efficiency and thoroughness of the BFS approach.

## Function Definitions
'generate_puzzle(difficulty):' Creates a random Sudoku puzzle according to the chosen difficulty.
'find_empty(board):' Identifies the first empty cell in the Sudoku board for the BFS to explore.
'redraw_window(win, board, time, strikes):' Updates the game window with the latest game status.
'format_time(secs):' Converts elapsed seconds into a human-readable format.
'main():' Initializes the game, handles event processing, and maintains the game loop.

##Classes
'Cube:' Manages individual cells in the Sudoku grid, handling cell state and rendering.
'Grid:' Manages the entire Sudoku grid, including methods for cell updates, puzzle solving, and drawing operations.

##Explanation:
The generate_puzzle function creates puzzles that are uniquely challenging by adjusting the number of prefilled cells based on the difficulty level.

The BFS approach ensures that all possible configurations of the Sudoku grid are explored systematically, starting from the shallowest level and expanding deeper until the solution is found.
The main function orchestrates the game's execution, from initialization through user interaction to the final solution display.
