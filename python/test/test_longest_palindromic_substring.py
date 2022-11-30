import unittest
from src.longest_palindromic_substring import Solution


class Tests(unittest.TestCase):

    def test_a1(self):
        s = "babad"
        test_result = "bab"
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.longestPalindrome(s))

    def test_a2(self):
        s = "cbbd"
        test_result = "bb"
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.longestPalindrome(s))

    def test_a3(self):
        s = "ac"
        test_result = "a"
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.longestPalindrome(s))

    def test_a4(self):
        s = "abb"
        test_result = "bb"
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.longestPalindrome(s))


if __name__ == "__main__":
    unittest.main()
