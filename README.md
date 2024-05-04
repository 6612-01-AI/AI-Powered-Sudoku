# AI-Powered-Sudoku Solver
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

# Algorithm Descriptions
Breadth-First Search (BFS): A level-order search algorithm that explores all nodes at the present depth prior to moving on to nodes at the next depth level. Efficient for finding the shortest path in terms of the number of moves.

Depth-First Search (DFS): An algorithm that explores as far as possible along each branch before backtracking. It's effective for space-limited scenarios but not always optimal for finding the shortest path.

Iterative Deepening Search (IDS): Combines the space efficiency of DFS with the optimality of BFS. It incrementally explores all nodes at increasing depth levels.

Constraint Satisfaction Problem (CSP): This approach applies problem-solving techniques by identifying and enforcing constraints for each step in the Sudoku grid, effectively reducing the number of guesses needed.

# Analysis
While running each algorithm, the number of backtrack and time taken to solve each file is is stored in a text file, which also has the presvious logs. Also, there is another python give which is capable to evlauate the average time taken and average number of bracktracks needed by each algorithm. These files can be used to find which algorithm can solve the sudoku puzzle more efficiently.
