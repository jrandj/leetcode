from src.maximum_subarray import Solution

import unittest


class Tests(unittest.TestCase):
    def test_1a(self):
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        test_result = 6
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.maxSubArray_naive(nums))

    def test_2a(self):
        nums = [1]
        test_result = 1
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.maxSubArray_naive(nums))

    def test_3a(self):
        nums = [5, 4, -1, 7, 8]
        test_result = 23
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.maxSubArray_naive(nums))

    def test_4a(self):
        nums = [-1, -2]
        test_result = -1
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.maxSubArray_naive(nums))

    def test_1b(self):
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        test_result = 6
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.maxSubArray_dp(nums))

    def test_2b(self):
        nums = [1]
        test_result = 1
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.maxSubArray_dp(nums))

    def test_3b(self):
        nums = [5, 4, -1, 7, 8]
        test_result = 23
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.maxSubArray_dp(nums))

    def test_4b(self):
        nums = [-1, -2]
        test_result = -1
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.maxSubArray_dp(nums))


if __name__ == "__main__":
    unittest.main()
