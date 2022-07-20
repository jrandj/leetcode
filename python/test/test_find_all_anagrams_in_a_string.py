import unittest
from src.find_all_anagrams_in_a_string import Solution


class Tests(unittest.TestCase):
    def test_1(self):
        s = "cbaebabacd"
        p = "abc"
        test_result = [0, 6]
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.findAnagrams(s, p))

    def test_2(self):
        s = "abab"
        p = "ab"
        test_result = [0, 1, 2]
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.findAnagrams(s, p))


if __name__ == '__main__':
    unittest.main()
