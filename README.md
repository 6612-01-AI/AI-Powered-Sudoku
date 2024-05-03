# AI-Powered-Sudoku
Welcome to the Sudoku Solver project! This Python-powered application utilizes the Pygame library to craft an interactive graphical user interface (GUI) for tackling Sudoku puzzles. Whether you're keen on honing your Sudoku-solving prowess or just seeking a delightful pastime, this solver provides both manual puzzle-solving and automated solving functionalities.

Leveraging a blend of backtracking algorithms and constraint satisfaction methods, the solver adeptly navigates through Sudoku puzzles to find solutions. With its ability to generate random Sudoku puzzles across different difficulty levels and intuitive input mechanisms, users can relish a personalized Sudoku-solving journey tailored to their liking and proficiency level.

## Environment Setup
  ### Required Python Version
  Use `Python 3.11` 

  ### Requisite Library
  ```
  import pygame
  import random
  import time 
  ```
  ### Custom Package

  ```
  from solver_CSP import solve, valid
  from solver_DFS import solve_dfs, valid
  from solver_IDS import iterative_deepening_solve, valid

  ```
## Execute

# AI Solver Input
| Keys              | Actions                                                          |
|-------------------|------------------------------------------------------------------|
|`Space`  	    | Solve the Sudoku puzzle using the algorithm.                     |
|`Enter`            | Confirm the value written on the board.		               |

  
