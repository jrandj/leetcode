import unittest
from src.valid_parentheses import Solution


class Tests(unittest.TestCase):
    def test_a1(self):
        s = "()"
        actual_result = Solution.isValid(self, s)
        test_result = True
        self.assertEqual(test_result, actual_result)

    def test_a2(self):
        s = "()[]{}"
        actual_result = Solution.isValid(self, s)
        test_result = True
        self.assertEqual(test_result, actual_result)

    def test_a3(self):
        s = "(]"
        actual_result = Solution.isValid(self, s)
        test_result = False
        self.assertEqual(test_result, actual_result)

    def test_a4(self):
        s = "([)]"
        actual_result = Solution.isValid(self, s)
        test_result = False
        self.assertEqual(test_result, actual_result)

    def test_a5(self):
        s = "]"
        actual_result = Solution.isValid(self, s)
        test_result = False
        self.assertEqual(test_result, actual_result)


if __name__ == '__main__':
    unittest.main()
