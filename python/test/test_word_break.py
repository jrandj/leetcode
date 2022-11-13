import unittest

from src.word_break import Solution


class Tests(unittest.TestCase):
    def test_1a(self):
        s = "leetcode"
        wordDict = ["leet", "code"]
        actual_result = Solution()
        self.assertTrue(actual_result.wordBreak_recursive(s, wordDict))

    def test_2a(self):
        s = "applepenapple"
        wordDict = ["apple", "pen"]
        actual_result = Solution()
        self.assertTrue(actual_result.wordBreak_recursive(s, wordDict))

    def test_3a(self):
        s = "catsandog"
        wordDict = ["cats", "dog", "sand", "and", "cat"]
        actual_result = Solution()
        self.assertFalse(actual_result.wordBreak_recursive(s, wordDict))

    def test_1b(self):
        s = "leetcode"
        wordDict = ["leet", "code"]
        actual_result = Solution()
        self.assertTrue(actual_result.wordBreak_iterative(s, wordDict))

    def test_2b(self):
        s = "applepenapple"
        wordDict = ["apple", "pen"]
        actual_result = Solution()
        self.assertTrue(actual_result.wordBreak_iterative(s, wordDict))

    def test_3b(self):
        s = "catsandog"
        wordDict = ["cats", "dog", "sand", "and", "cat"]
        actual_result = Solution()
        self.assertFalse(actual_result.wordBreak_iterative(s, wordDict))

    def test_4b(self):
        s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
        wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
        actual_result = Solution()
        self.assertFalse(actual_result.wordBreak_iterative(s, wordDict))
