"""http://en.wikipedia.org/wiki/Eight_queens_puzzle
"""

import sys

def solve(size, queens=None):
    queens = queens or []
    col = len(queens)

    if col == size:
        return queens

    for row in range(size):
        # Check if a queen is on the same row.
        if row in queens:
            continue

        # Check if a queen is on the same diagonal.
        same_diag = False
        for (other_col, other_row) in enumerate(queens):
            norm_row = row - other_row
            norm_col = col - other_col

            if norm_col == norm_row or norm_col == -norm_row:
                same_diag = True
                break

        if same_diag:
            continue

        solution = solve(size, queens + [row])

        if solution is not None:
            return solution

    return None

if __name__ == '__main__':
    size = int(sys.argv[1])
    solution = solve(size)

    board = [['_'] * size for i in range(size)]

    for col, row in enumerate(solution):
        board[row][col] = 'X'

    for row in board:
        print ' '.join(row)
