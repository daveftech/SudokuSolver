# SudokuSolver
An application for solving sudoku puzzles

Input: 9 x 9 matrix
Solution: 9 x 9 matrix

Algorithm:
Initialize solution to all zeros
Populate solution with values from Input
For each non-zero cell, determine possible values
- Is there only one possible value for the current cell?
    - Yes: Set this in the solution
- Is the puzzle is solved?
    - Yes: print result
    - No: move on to the next cell
