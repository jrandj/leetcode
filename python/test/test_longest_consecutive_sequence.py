import unittest

from src.longest_consecutive_sequence import Solution


class Tests(unittest.TestCase):
    def test_1(self):
        nums = [100, 4, 200, 1, 3, 2]
        test_result = 4
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.longestConsecutive(nums))

    def test_2(self):
        nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
        test_result = 9
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.longestConsecutive(nums))


if __name__ == "__main__":
    unittest.main()
