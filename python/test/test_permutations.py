from src.permutations import Solution

import unittest


class Tests(unittest.TestCase):
    def test_1(self):
        nums = [1, 2, 3]
        test_result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        actual_result = Solution()
        self.assertCountEqual(test_result, actual_result.permute(nums))

    def test_2(self):
        nums = [1]
        test_result = [[1]]
        actual_result = Solution()
        self.assertCountEqual(test_result, actual_result.permute(nums))


if __name__ == '__main__':
    unittest.main()
