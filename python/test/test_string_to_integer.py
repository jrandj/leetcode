import unittest
from src.string_to_integer import Solution


class Tests(unittest.TestCase):
    def test_a1(self):
        s = "42"
        test_result = 42
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.myAtoi(s))

    def test_a2(self):
        s = "   -42"
        test_result = -42
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.myAtoi(s))

    def test_a3(self):
        s = "4193 with words"
        test_result = 4193
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.myAtoi(s))

    def test_a4(self):
        s = "words and 987"
        test_result = 0
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.myAtoi(s))

    def test_a5(self):
        s = "-91283472332"
        test_result = -2147483648
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.myAtoi(s))

    def test_a6(self):
        s = "2147483648"
        test_result = 2147483647
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.myAtoi(s))


if __name__ == '__main__':
    unittest.main()
