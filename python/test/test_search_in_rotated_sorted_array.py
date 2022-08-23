import unittest
from src.search_in_rotated_sorted_array import Solution


class Tests(unittest.TestCase):
    def test_1(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        test_result = 4
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.search(nums, target))

    def test_2(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 3
        test_result = -1
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.search(nums, target))

    def test_3(self):
        nums = [1]
        target = 0
        test_result = -1
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.search(nums, target))

    def test_4(self):
        nums = [5, 1, 3]
        target = 3
        test_result = 2
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.search(nums, target))


if __name__ == "__main__":
    unittest.main()
