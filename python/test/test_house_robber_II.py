from src.house_robber_II import Solution

import unittest


class Tests(unittest.TestCase):
    def test_1(self):
        nums = [2, 3, 2]
        test_result = 3
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.rob(nums))

    def test_2(self):
        nums = [1, 2, 3, 1]
        test_result = 4
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.rob(nums))

    def test_3(self):
        nums = [1, 2, 3]
        test_result = 3
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.rob(nums))


if __name__ == '__main__':
    unittest.main()
