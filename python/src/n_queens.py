from typing import List


class Solution:
    """
    The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each
    other.

    Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

    Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a
    queen and an empty space, respectively.
    """

    def __init__(self):
        """
        Initialise the solution.
        """
        self.col = set()
        self.pos_diag = set()  # (r + c)
        self.neg_diag = set()  # (r - c)
        self.res = []
        self.board = None

    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        Given an integer n, return all distinct solutions to the n-queens puzzle.

        :param n: The length and width of the board.
        :type n: Int.
        :return: The list of solutions.
        :rtype: List[List[Str]].

        The time complexity is O(N!). Faster than 50.75% of solutions.

        The time complexity is O(N) for the sets and recursive function calls. Less memory than 14.06% of solutions.
        """
        self.board = [['.'] * n for i in range(n)]
        self.backtrack(0, n)
        return self.res

    def backtrack(self, r: int, n: int):
        """
        A helper method for backtracking.

        :param r: The current row.
        :type r: Int.
        :param n: The length and width of the board.
        :type n: Int.
        :return: NoneType.
        :rtype: NoneType.
        """
        # base case (we reached the last row of the board)
        if r == n:
            row_copy = ["".join(row) for row in self.board]
            self.res.append(row_copy)
            return

        # for each column
        for c in range(n):
            # skip if current position is not possible
            if c in self.col or (r + c) in self.pos_diag or (r - c) in self.neg_diag:
                continue

            # take the current cell
            self.board[r][c] = 'Q'
            self.col.add(c)
            self.pos_diag.add(r + c)
            self.neg_diag.add(r - c)

            self.backtrack(r + 1, n)

            # clear the current cell
            self.col.remove(c)
            self.pos_diag.remove(r + c)
            self.neg_diag.remove(r - c)
            self.board[r][c] = '.'
