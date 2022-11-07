from src.coin_change import Solution

import unittest


class Tests(unittest.TestCase):
    def test_1(self):
        coins = [1, 2, 5]
        amount = 11
        test_result = 3
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.coinChange_recursive(coins, amount))

    def test_2(self):
        coins = [2]
        amount = 3
        test_result = -1
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.coinChange_recursive(coins, amount))

    def test_3(self):
        coins = [1]
        amount = 0
        test_result = 0
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.coinChange_recursive(coins, amount))

    def test_4(self):
        coins = [186, 419, 83, 408]
        amount = 6249
        test_result = 20
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.coinChange_recursive(coins, amount))

    def test_5(self):
        coins = [1, 2, 5]
        amount = 11
        test_result = 3
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.coinChange_iterative(coins, amount))

    def test_6(self):
        coins = [2]
        amount = 3
        test_result = -1
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.coinChange_iterative(coins, amount))

    def test_7(self):
        coins = [1]
        amount = 0
        test_result = 0
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.coinChange_iterative(coins, amount))

    def test_8(self):
        coins = [186, 419, 83, 408]
        amount = 6249
        test_result = 20
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.coinChange_iterative(coins, amount))
