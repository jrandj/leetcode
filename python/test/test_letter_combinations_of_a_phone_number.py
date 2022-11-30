from src.letter_combinations_of_a_phone_number import Solution

import unittest


class Tests(unittest.TestCase):
    def test_1(self):
        digits = "23"
        test_result = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        actual_result = Solution()
        self.assertCountEqual(test_result, actual_result.letterCombinations(digits))

    def test_2(self):
        digits = ""
        test_result = []
        actual_result = Solution()
        self.assertCountEqual(test_result, actual_result.letterCombinations(digits))

    def test_3(self):
        digits = "2"
        test_result = ["a", "b", "c"]
        actual_result = Solution()
        self.assertCountEqual(test_result, actual_result.letterCombinations(digits))


if __name__ == '__main__':
    unittest.main()
