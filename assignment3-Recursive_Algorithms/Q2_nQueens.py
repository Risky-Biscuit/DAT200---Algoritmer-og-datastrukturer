"""
DAT200 - Assignment 3 (Q2): N-Queens
Return all distinct solutions as lists of strings with 'Q' and '.'.
"""

from typing import List


def solve_n_queens(n: int) -> List[List[str]]:
    """
    Backtracking:
      - place one queen per row
      - track used columns and diagonals:
          diag1: r - c (↘), diag2: r + c (↙)
    """
    if n <= 0:
        return []
    if n in (2, 3):  # Known: no solutions exist for 2 or 3
        return []

    cols = set()
    diag1 = set()  # r - c
    diag2 = set()  # r + c
    board = [["."] * n for _ in range(n)]
    solutions: List[List[str]] = []

    # Safety check: a queen at (r, c) must not share a column or giagonal with any existing queen
    def can_place(r: int, c: int) -> bool:
        return (c not in cols) and ((r - c) not in diag1) and ((r + c) not in diag2)

    def backtrack(r: int) -> None:
        if r == n:
            solutions.append(["".join(row) for row in board])
            return
        for c in range(n):
            if not can_place(r, c):
                continue
            # place a queen at (r, c) and mark its column + diagonals as used
            board[r][c] = "Q"
            cols.add(c)
            diag1.add(r - c)
            diag2.add(r + c)
            # recurse to try placing the next row
            backtrack(r + 1)
            # backtrack: undo the placement to try the next column in this row
            board[r][c] = "."
            cols.remove(c)
            diag1.remove(r - c)
            diag2.remove(r + c)

    backtrack(0)
    return solutions


if __name__ == "__main__":
    try:
        n = int(input("How many squares? "))
    except ValueError:
        print("Pleace enter an integer.")
        exit(1)

    sols = solve_n_queens(n)
    print(f"n={n} -> {len(sols)} solutions")
    for s in sols:
        print(*s, sep="\n")
        print("-")
