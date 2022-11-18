import unittest

from src.partition_equal_subset_sum import Solution


class Tests(unittest.TestCase):
    def test_1a(self):
        nums = [1, 5, 11, 5]
        actual_result = Solution()
        self.assertTrue(actual_result.canPartition_recursive(nums))

    def test_2a(self):
        nums = [1, 2, 3, 5]
        actual_result = Solution()
        self.assertFalse(actual_result.canPartition_recursive(nums))

    def test_3a(self):
        nums = [3, 3, 3, 4, 5]
        actual_result = Solution()
        self.assertTrue(actual_result.canPartition_recursive(nums))

    def test_4a(self):
        nums = [1, 5, 3]
        actual_result = Solution()
        self.assertFalse(actual_result.canPartition_recursive(nums))

    def test_1b(self):
        nums = [1, 5, 11, 5]
        actual_result = Solution()
        self.assertTrue(actual_result.canPartition_iterative(nums))

    def test_2b(self):
        nums = [1, 2, 3, 5]
        actual_result = Solution()
        self.assertFalse(actual_result.canPartition_iterative(nums))

    def test_3b(self):
        nums = [3, 3, 3, 4, 5]
        actual_result = Solution()
        self.assertTrue(actual_result.canPartition_iterative(nums))

    def test_4b(self):
        nums = [1, 5, 3]
        actual_result = Solution()
        self.assertFalse(actual_result.canPartition_iterative(nums))


if __name__ == '__main__':
    unittest.main()
