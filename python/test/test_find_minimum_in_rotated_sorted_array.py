import unittest

from src.find_minimum_in_rotated_sorted_array import Solution


class Tests(unittest.TestCase):
    def test_1(self):
        nums = [3, 4, 5, 1, 2]
        test_result = 1
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.findMin(nums))

    def test_2(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        test_result = 0
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.findMin(nums))

    def test_3(self):
        nums = [11, 13, 15, 17]
        test_result = 11
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.findMin(nums))


if __name__ == "__main__":
    unittest.main()
