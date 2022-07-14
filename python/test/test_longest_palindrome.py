import unittest
from src.longest_palindrome import Solution


class Tests(unittest.TestCase):
    def test_a1(self):
        s = "abccccdd"
        test_result = 7
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.longestPalindrome(s))

    def test_a2(self):
        s = "a"
        test_result = 1
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.longestPalindrome(s))


if __name__ == "__name__":
    unittest.main()
