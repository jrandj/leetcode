import unittest

from src.target_sum import Solution


class Tests(unittest.TestCase):
    def test_1(self):
        nums = [1, 1, 1, 1, 1]
        target = 3
        test_result = 5
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.findTargetSumWays(nums, target))

    def test_2(self):
        nums = [1]
        target = 1
        test_result = 1
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.findTargetSumWays(nums, target))


if __name__ == "__main__":
    unittest.main()
