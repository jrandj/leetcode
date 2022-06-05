import unittest
from src.three_sum import Solution


class Tests(unittest.TestCase):
    def test_a1(self):
        nums = [-1, 0, 1, 2, -1, -4]
        actual_result = Solution.threeSum(self, nums)
        test_result = [[-1, -1, 2], [-1, 0, 1]]
        self.assertEqual(test_result, actual_result)

    def test_a2(self):
        nums = []
        actual_result = Solution.threeSum(self, nums)
        test_result = []
        self.assertEqual(test_result, actual_result)

    def test_a3(self):
        nums = [0]
        actual_result = Solution.threeSum(self, nums)
        test_result = []
        self.assertEqual(test_result, actual_result)


if __name__ == '__main__':
    unittest.main()
