import unittest
from src.evaluate_reverse_polish_notation import Solution


class Tests(unittest.TestCase):
    def test_a1(self):
        tokens = ["2", "1", "+", "3", "*"]
        actual_result = Solution.evalRPN(self, tokens)
        test_result = 9
        self.assertEqual(test_result, actual_result)

    def test_a2(self):
        tokens = ["4", "13", "5", "/", "+"]
        actual_result = Solution.evalRPN(self, tokens)
        test_result = 6
        self.assertEqual(test_result, actual_result)

    def test_a3(self):
        tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        actual_result = Solution.evalRPN(self, tokens)
        test_result = 22
        self.assertEqual(test_result, actual_result)


if __name__ == '__main__':
    unittest.main()
