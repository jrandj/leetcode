from src.maximum_product_subarray import Solution

import unittest


class Tests(unittest.TestCase):
    def test_1a(self):
        nums = [2, 3, -2, 4]
        test_result = 6
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.maxProduct_naive(nums))

    def test_2a(self):
        nums = [-2, 0, -1]
        test_result = 0
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.maxProduct_naive(nums))

    def test_3a(self):
        nums = [-2]
        test_result = -2
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.maxProduct_naive(nums))

    def test_4a(self):
        nums = [0, 2]
        test_result = 2
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.maxProduct_naive(nums))

    def test_5a(self):
        nums = [3, -1, 4]
        test_result = 4
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.maxProduct_naive(nums))

    def test_1b(self):
        nums = [2, 3, -2, 4]
        test_result = 6
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.maxProduct_dynamic(nums))

    def test_2b(self):
        nums = [-2, 0, -1]
        test_result = 0
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.maxProduct_dynamic(nums))

    def test_3b(self):
        nums = [-2]
        test_result = -2
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.maxProduct_dynamic(nums))

    def test_4b(self):
        nums = [0, 2]
        test_result = 2
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.maxProduct_dynamic(nums))

    def test_5b(self):
        nums = [3, -1, 4]
        test_result = 4
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.maxProduct_dynamic(nums))


if __name__ == '__main__':
    unittest.main()
