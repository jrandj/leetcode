import unittest
from src.best_time_to_buy_and_sell_stock import Solution


class Tests(unittest.TestCase):
    def test_1(self):
        nums = [7, 1, 5, 3, 6, 4]
        actual_result = Solution.maxProfit(self, nums)
        test_result = 5
        self.assertEqual(test_result, actual_result)

    def test_2(self):
        nums = [7, 6, 4, 3, 1]
        actual_result = Solution.maxProfit(self, nums)
        test_result = 0
        self.assertEqual(test_result, actual_result)

    def test_3(self):
        nums = [2, 1, 2, 1, 0, 1, 2]
        actual_result = Solution.maxProfit(self, nums)
        test_result = 2
        self.assertEqual(test_result, actual_result)


if __name__ == '__main__':
    unittest.main()
