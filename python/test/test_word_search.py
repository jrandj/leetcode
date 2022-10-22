from src.word_search import Solution

import unittest


class Tests(unittest.TestCase):
    def test_1(self):
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = "ABCCED"
        actual_result = Solution()
        self.assertTrue(actual_result.exist(board, word))

    def test_2(self):
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = "ABCCED"
        actual_result = Solution()
        self.assertTrue(actual_result.exist(board, word))

    def test_3(self):
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = "ABCB"
        actual_result = Solution()
        self.assertFalse(actual_result.exist(board, word))


if __name__ == '__main__':
    unittest.main()
