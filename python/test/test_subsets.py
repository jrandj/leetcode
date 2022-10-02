from src.subsets import Solution
import unittest


class Tests(unittest.TestCase):
    def test_1(self):
        nums = [1, 2, 3]
        test_result = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        actual_result = Solution()
        self.assertCountEqual(test_result, actual_result.subsets(nums))

    def test_2(self):
        nums = [0]
        test_result = [[], [0]]
        actual_result = Solution()
        self.assertCountEqual(test_result, actual_result.subsets(nums))


if __name__ == '__main__':
    unittest.main()
