import unittest

from src.permutation_in_string import Solution


class Tests(unittest.TestCase):
    def test1(self):
        s1 = "ab"
        s2 = "eidbaooo"
        test_result = True
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.checkInclusion(s1, s2))

    def test2(self):
        s1 = "ab"
        s2 = "eidboaoo"
        test_result = False
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.checkInclusion(s1, s2))

    def test3(self):
        s1 = "abc"
        s2 = "ccccbbbbaaaa"
        test_result = False
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.checkInclusion(s1, s2))
