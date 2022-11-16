from src.best_time_to_buy_and_sell_stock_with_cooldown import Solution

import unittest


class Tests(unittest.TestCase):
    def test_1a(self):
        prices = [1, 2, 3, 0, 2]
        test_result = 3
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.maxProfit_recursion(prices))

    def test_2a(self):
        prices = [1]
        test_result = 0
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.maxProfit_recursion(prices))

    def test_1b(self):
        prices = [1, 2, 3, 0, 2]
        test_result = 3
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.maxProfit_dfs(prices))

    def test_2b(self):
        prices = [1]
        test_result = 0
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.maxProfit_dfs(prices))


if __name__ == "__main__":
    unittest.main()
