from src.subsets_ii import Solution

import unittest


class Tests(unittest.TestCase):
    def test_1(self):
        test_result = [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
        nums = [1, 2, 2]
        actual_result = Solution()
        self.assertCountEqual(test_result, actual_result.subsetsWithDup(nums))

    def test_2(self):
        test_result = [[], [0]]
        nums = [0]
        actual_result = Solution()
        self.assertCountEqual(test_result, actual_result.subsetsWithDup(nums))

    def test_3(self):
        test_result = [[], [1], [1, 4], [1, 4, 4], [1, 4, 4, 4], [1, 4, 4, 4, 4], [4], [4, 4], [4, 4, 4], [4, 4, 4, 4]]
        nums = [4, 4, 4, 1, 4]
        actual_result = Solution()
        self.assertCountEqual(test_result, actual_result.subsetsWithDup(nums))


if __name__ == '__main__':
    unittest.main()
