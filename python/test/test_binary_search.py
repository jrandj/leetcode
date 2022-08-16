import unittest
from src.binary_search import Solution


class Tests(unittest.TestCase):

    def test_1(self):
        nums = [-1, 0, 3, 5, 9, 12]
        target = 9
        test_result = 4
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.search(nums, target))

    def test_2(self):
        nums = [-1, 0, 3, 5, 9, 12]
        target = 2
        test_result = -1
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.search(nums, target))


if __name__ == '__main__':
    unittest.main()
