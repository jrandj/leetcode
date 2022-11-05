import unittest

from src.longest_increasing_subsequence import Solution


class Tests(unittest.TestCase):
    def test_1a(self):
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        test_result = 4
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.lengthOfLIS_naive(nums))

    def test_2a(self):
        nums = [0, 1, 0, 3, 2, 3]
        test_result = 4
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.lengthOfLIS_naive(nums))

    def test_3a(self):
        nums = [7, 7, 7, 7, 7, 7, 7]
        test_result = 1
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.lengthOfLIS_naive(nums))

    def test_4a(self):
        nums = [3, 1, 2]
        test_result = 2
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.lengthOfLIS_naive(nums))

    def test_5a(self):
        nums = [4, 10, 4, 3, 8, 9]
        test_result = 3
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.lengthOfLIS_naive(nums))

    def test_1b(self):
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        test_result = 4
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.lengthOfLIS_iterative(nums))

    def test_2b(self):
        nums = [0, 1, 0, 3, 2, 3]
        test_result = 4
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.lengthOfLIS_iterative(nums))

    def test_3b(self):
        nums = [7, 7, 7, 7, 7, 7, 7]
        test_result = 1
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.lengthOfLIS_iterative(nums))

    def test_4b(self):
        nums = [3, 1, 2]
        test_result = 2
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.lengthOfLIS_iterative(nums))

    def test_5b(self):
        nums = [4, 10, 4, 3, 8, 9]
        test_result = 3
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.lengthOfLIS_iterative(nums))

    def test_1c(self):
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        test_result = 4
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.lengthOfLIS_naive_memo(nums))

    def test_2c(self):
        nums = [0, 1, 0, 3, 2, 3]
        test_result = 4
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.lengthOfLIS_naive_memo(nums))

    def test_3c(self):
        nums = [7, 7, 7, 7, 7, 7, 7]
        test_result = 1
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.lengthOfLIS_naive_memo(nums))

    def test_4c(self):
        nums = [3, 1, 2]
        test_result = 2
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.lengthOfLIS_naive_memo(nums))

    def test_5c(self):
        nums = [4, 10, 4, 3, 8, 9]
        test_result = 3
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.lengthOfLIS_naive_memo(nums))


if __name__ == '__main__':
    unittest.main()
