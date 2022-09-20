import unittest
from src.two_sum_ii import Solution


class Tests(unittest.TestCase):
    def test_1(self):
        numbers = [2, 7, 11, 15]
        target = 9
        actual_result = Solution()
        test_result = [1, 2]
        self.assertEqual(test_result, actual_result.twoSum(numbers, target))

    def test_2(self):
        numbers = [2, 3, 4]
        target = 6
        actual_result = Solution()
        test_result = [1, 3]
        self.assertEqual(test_result, actual_result.twoSum(numbers, target))

    def test_3(self):
        numbers = [-1, 0]
        target = -1
        actual_result = Solution()
        test_result = [1, 2]
        self.assertEqual(test_result, actual_result.twoSum(numbers, target))


if __name__ == '__main__':
    unittest.main()
