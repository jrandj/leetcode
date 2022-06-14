import unittest
from src.sort_colors import Solution


class Tests(unittest.TestCase):
    def test_a1(self):
        nums = [2, 0, 2, 1, 1, 0]
        Solution.sortColors(self, nums)
        test_result = [0, 0, 1, 1, 2, 2]
        self.assertEqual(nums, test_result)

    def test_a2(self):
        nums = [2, 0, 1]
        Solution.sortColors(self, nums)
        test_result = [0, 1, 2]
        self.assertEqual(nums, test_result)


if __name__ == '__main__':
    unittest.main()
