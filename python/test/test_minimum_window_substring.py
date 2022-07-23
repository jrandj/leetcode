import unittest
from src.minimum_window_substring import Solution


class Tests(unittest.TestCase):

    def test_1(self):
        s = "ADOBECODEBANC"
        t = "ABC"
        test_result = "BANC"
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.minWindow(s, t))

    def test_2(self):
        s = "a"
        t = "a"
        test_result = "a"
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.minWindow(s, t))

    def test_3(self):
        s = "a"
        t = "aa"
        test_result = ""
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.minWindow(s, t))

    def test_4(self):
        s = "aa"
        t = "aa"
        test_result = "aa"
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.minWindow(s, t))


if __name__ == "__main__":
    unittest.main()
