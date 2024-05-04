# AI-Powered-Sudoku
Welcome to the AI-Powered Sudoku Solver project by Team Yash & Parin from the University of New Haven. This AI-driven application leverages advanced search algorithms to efficiently solve Sudoku puzzles and offers a user-friendly graphical interface for interactive puzzle solving and visualization.

## Project Highlights
AI Model: Employs advanced AI to solve puzzles quickly.

Interactive GUI: Built with Pygame for easy puzzle input and solution visualization.

Version Control: Managed with Git for collaborative and systematic development.

For more details on setup and usage, please see the sections below.

## Files Overview
GUI.py: Manages the graphical user interface for user interaction and puzzle display.

metrics_performance.py: Analyzes and reports performance metrics of the solver, such as average time and recursive calls.

solver_IDS.py: Implements the Sudoku solver using Iterative Deepening Search (IDS) to solve puzzles.

metrics_performance.txt: Stores averaged performance data like recursive calls and solving time.

sudoku_IDS_solver_output.txt: Logs detailed performance data for each puzzle solved, including recursive calls and time taken.

## Environment Setup
  ### Required Python Version
  Use `Python 3.11` 

  ### Requisite Library
  ```
  import pygame
  import random
  import time
  import deepcopy
  ```
  ### Custom Package

  ```
  from solver_CSP import solve, valid
  from solver_DFS import solve_dfs, valid
  from solver_IDS import iterative_deepening_solve, valid
  from solver_DFS import solve_bfs, valid
  ```
  For every algorithm there is a different GUI and solver file. So, make sure both the file are available in the same directory.
## Execute
Place all the necessary files in the same directory. To start the application, run the following command in your terminal:
```
python GUI.py
```

# AI Solver Input
| Keys              | Actions                                                          |
|-------------------|------------------------------------------------------------------|
|`Space`  	        | Press it to solve the Sudoku puzzle using the algorithm.         |
  
