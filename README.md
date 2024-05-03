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

## Input required for execture the code
### End player
| Keys              | Actions                                                          |
|-------------------|------------------------------------------------------------------|
|`1`                | Enter the number 1 into the selected cell.                       |
|`2`                | Enter the number 2 into the selected cell.                       |
|`3`                | Enter the number 3 into the selected cell.                       |
|`4`                | Enter the number 4 into the selected cell.                       |
|`5`                | Enter the number 5 into the selected cell.                       |
|`6`                | Enter the number 6 into the selected cell.                       |
|`7`                | Enter the number 7 into the selected cell.                       |
|`8`                | Enter the number 8 into the selected cell.                       |
|`9`                | Enter the number 9 into the selected cell.                       |
|`Keypad 1`         | Enter the number 1 into the selected cell.                       |
|`Keypad 2`         | Enter the number 2 into the selected cell.                       |
|`Keypad 3`         | Enter the number 3 into the selected cell.                       |
|`Keypad 4`         | Enter the number 4 into the selected cell.                       |
|`Keypad 5`         | Enter the number 5 into the selected cell.                       |
|`Keypad 6`         | Enter the number 6 into the selected cell.                       |
|`Keypad 7`         | Enter the number 7 into the selected cell.                       |
|`Keypad 8`         | Enter the number 8 into the selected cell.                       |
|`Keypad 9`         | Enter the number 9 into the selected cell.                       |
|`Backspace/Delete` | Clear the value in the selected cell.                            |
|`Left Click`       | Select a box to enter a value into that cell.                    |
|`h`                | Display a random correct value on the board as a hint.           |

# AI Solver Input
| Keys              | Actions                                                          |
|-------------------|------------------------------------------------------------------|
|`Space`   | Solve the Sudoku puzzle using the algorithm.                              |
|`Enter`   | Confirm the value written on the board.				       |
		
