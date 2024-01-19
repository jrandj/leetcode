from src.longest_repeating_character_replacement import Solution

import unittest


class Test(unittest.TestCase):
    def test_1(self):
        test_result = 4
        s = "ABAB"
        k = 2
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.characterReplacement(s, k))

    def test_2(self):
        test_result = 4
        s = "AABABBA"
        k = 1
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.characterReplacement(s, k))


if __name__ == "__main__":
    unittest.main()
