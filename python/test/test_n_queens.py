from src.n_queens import Solution

import unittest


class Tests(unittest.TestCase):
    def test_1(self):
        n = 4
        test_result = [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]
        actual_result = Solution()
        self.assertCountEqual(test_result, actual_result.solveNQueens(n))

    def test_2(self):
        n = 1
        test_result = [["Q"]]
        actual_result = Solution()
        self.assertCountEqual(test_result, actual_result.solveNQueens(n))
