import unittest
from src.basic_calculator import Solution


class Tests(unittest.TestCase):
    def test_a1(self):
        s = "1 + 1"
        actual_result = Solution()
        test_result = 2
        self.assertEqual(test_result, actual_result.calculate(s))

    def test_a2(self):
        s = " 2-1 + 2 "
        actual_result = Solution()
        test_result = 3
        self.assertEqual(test_result, actual_result.calculate(s))

    def test_a3(self):
        s = "(1+(4+5+2)-3)+(6+8)"
        actual_result = Solution()
        test_result = 23
        self.assertEqual(test_result, actual_result.calculate(s))

    def test_a4(self):
        s = ""
        actual_result = Solution()
        test_result = 0
        self.assertEqual(test_result, actual_result.calculate(s))

    def test_a5(self):
        s = "badstring"
        actual_result = Solution()
        test_result = 0
        self.assertEqual(test_result, actual_result.calculate(s))

    def test_a6(self):
        s = "2147483647"
        actual_result = Solution()
        test_result = 2147483647
        self.assertEqual(test_result, actual_result.calculate(s))


if __name__ == '__main__':
    unittest.main()
