import unittest
from src.longest_substring_without_repeating_characters import Solution


class Tests(unittest.TestCase):
    def test_a1(self):
        s = "abcabcbb"
        test_result = 3
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.lengthOfLongestSubstring(s))

    def test_a2(self):
        s = "bbbbb"
        test_result = 1
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.lengthOfLongestSubstring(s))

    def test_a3(self):
        s = "pwwkew"
        test_result = 3
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.lengthOfLongestSubstring(s))

    def test_a4(self):
        s = "aab"
        test_result = 2
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.lengthOfLongestSubstring(s))

    def test_a5(self):
        s = "dvdf"
        test_result = 3
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.lengthOfLongestSubstring(s))


if __name__ == "__main__":
    unittest.main()
