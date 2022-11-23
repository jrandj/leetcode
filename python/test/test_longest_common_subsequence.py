import unittest
from src.longest_common_subsequence import Solution


class Tests(unittest.TestCase):

    def test_1a(self):
        test_result = 3
        text1 = "abcde"
        text2 = "ace"
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.longestCommonSubsequence_recursion(text1, text2))

    def test_2a(self):
        test_result = 3
        text1 = "abc"
        text2 = "abc"
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.longestCommonSubsequence_recursion(text1, text2))

    def test_3a(self):
        test_result = 0
        text1 = "abc"
        text2 = "def"
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.longestCommonSubsequence_recursion(text1, text2))

    def test_1b(self):
        test_result = 3
        text1 = "abcde"
        text2 = "ace"
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.longestCommonSubsequence_dp(text1, text2))

    def test_2b(self):
        test_result = 3
        text1 = "abc"
        text2 = "abc"
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.longestCommonSubsequence_dp(text1, text2))

    def test_3b(self):
        test_result = 0
        text1 = "abc"
        text2 = "def"
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.longestCommonSubsequence_dp(text1, text2))


if __name__ == "__main__":
    unittest.main()
