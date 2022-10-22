from typing import List


class Solution:
    """
    Given an m x n grid of characters board and a string word, return true if word exists in the grid.

    The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or
    vertically neighboring. The same letter cell may not be used more than once.
    """

    def __init__(self):
        self.board = None
        self.word = None
        self.cols = None
        self.rows = None
        self.path = None

    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Given an m x n grid of characters board and a string word, return true if word exists in the grid.

        :param board: The m x n board with each element containing a string.
        :type board: List[List[str]].
        :param word: The word that we are searching for.
        :type word: Str.
        :return: True if the word is found, and False otherwise.
        :rtype: Bool.

        The time complexity is O(m*n*4^(S)) where S is the length of the word. We iterate through each cell and
        there are 4 combinations for branching. Faster than 96.30% of solutions.

        The space complexity is O(S) due to the recursion. Less memory than 50.81% of solutions.
        """
        self.rows, self.cols = len(board), len(board[0])
        self.word, self.board = word, board
        self.path = set()

        if not self.check_if_possible(word, board):
            return False

        for r in range(self.rows):
            for c in range(self.cols):
                if self.dfs(r, c, 0):
                    return True
        return False

    def dfs(self, r: int, c: int, i: int):
        """
        A helper method to perform a Depth-First Search (DFS).

        :param r: The row index.
        :type r: Int.
        :param c: The column index.
        :type c: Int.
        :param i: The current index of the word.
        :type i: Int.
        :return: True if character at the current index of the word is on the board.
        :rtype: Bool.
        """
        # if we reach the end of the word we have found the word
        if i == len(self.word):
            return True
        # check the bounds, and that the character is in the word and unique
        elif r < 0 or c < 0 or r >= self.rows or c >= self.cols \
                or self.word[i] != self.board[r][c] or (r, c) in self.path:
            return False

        self.path.add((r, c))
        res = self.dfs(r + 1, c, i + 1) or self.dfs(r - 1, c, i + 1) \
              or self.dfs(r, c + 1, i + 1) or self.dfs(r, c - 1, i + 1)
        self.path.remove((r, c))
        return res

    def check_if_possible(self, word: str, board: List[List[str]]):
        """
        Used to perform a sanity check to reduce time complexity. If this returns False, there is no possible solution.

        :param word:
        :type word: Str.
        :param board:
        :type board: List[List[str]].
        :return: True if a solution is possible, and False otherwise.
        :rtype: Bool.
        """
        board_chars, word_chars = dict(), dict()
        for r in range(self.rows):
            for c in range(self.cols):
                board_chars[board[r][c]] = board_chars.get(board[r][c], 0) + 1

        for c in word:
            word_chars[c] = word_chars.get(c, 0) + 1

        for c in word:
            if word_chars.get(c, 0) and not board_chars.get(c, 0):
                return False
        return True
