from src.min_cost_climbing_stairs import Solution

import unittest


class Tests(unittest.TestCase):

    def test_1(self):
        cost = [10, 15, 20]
        test_result = 15
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.minCostClimbingStairs(cost))

    def test_2(self):
        cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
        test_result = 6
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.minCostClimbingStairs(cost))


if __name__ == '__main__':
    unittest.main()
