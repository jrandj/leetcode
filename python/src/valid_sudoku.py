import collections

from typing import List


class Solution:
    """
    Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following
    rules:
        - Each row must contain the digits 1-9 without repetition.
        - Each column must contain the digits 1-9 without repetition.
        - Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
    Note: A Sudoku board (partially filled) could be valid but is not necessarily solvable. Only the filled cells need
    to be validated according to the mentioned rules.
    """

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Determine if a 9 x 9 Sudoku board is valid.

        :param board: The Sudoku board.
        :type board: List[List[Str]].
        :return: True if the board represents a valid Sudoku board, and False otherwise.
        :rtype: Bool.

        The time complexity is O(N^2) where N is the dimension of the board. Faster than 79.86% of solutions.

        The space complexity is O(N) for the default dictionaries. Less memory than 34.20% of solutions.
        """
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(len(board[0])):
            for c in range(len(board)):
                # we don't need to check if it is emtpy
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                        board[r][c] in cols[c] or
                        board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True
