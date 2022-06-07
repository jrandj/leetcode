import unittest
from src.product_of_array_except_self import Solution


class Tests(unittest.TestCase):
    def test_a1(self):
        nums = [1, 2, 3, 4]
        actual_result = Solution.productExceptSelf(self, nums)
        test_result = [24, 12, 8, 6]
        self.assertEqual(test_result, actual_result)

    def test_a2(self):
        nums = [-1, 1, 0, -3, 3]
        actual_result = Solution.productExceptSelf(self, nums)
        test_result = [0, 0, 9, 0, 0]
        self.assertEqual(test_result, actual_result)


if __name__ == '__main__':
    unittest.main()
