from src.palindromic_substrings import Solution

import unittest


class Tests(unittest.TestCase):

    def test_1(self):
        s = "abc"
        test_result = 3
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.countSubstrings_1(s))

    def test_2(self):
        s = "aaa"
        test_result = 6
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.countSubstrings_1(s))

    def test_3(self):
        s = "abc"
        test_result = 3
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.countSubstrings_2(s))

    def test_4(self):
        s = "aaa"
        test_result = 6
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.countSubstrings_2(s))


if __name__ == '__main__':
    unittest.main()
