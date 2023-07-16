import unittest

from src.kth_largest_element_in_an_array import Solution


class Tests(unittest.TestCase):
    def test_1(self):
        nums = [3, 2, 1, 5, 6, 4]
        k = 2
        test_result = 5
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.findKthLargest(nums, k))

    def test_2(self):
        nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
        k = 4
        test_result = 4
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.findKthLargest(nums, k))


if __name__ == "__main__":
    unittest.main()
