import unittest

from src.generate_parenthesis import Solution


class Tests(unittest.TestCase):
    def test_1(self):
        n = 3
        test_result = ["((()))", "(()())", "(())()", "()(())", "()()()"]
        actual_result = Solution()
        self.assertCountEqual(test_result, actual_result.generateParenthesis(n))

    def test_2(self):
        n = 1
        test_result = ["()"]
        actual_result = Solution()
        self.assertCountEqual(test_result, actual_result.generateParenthesis(n))


if __name__ == "__main__":
    unittest.main()
