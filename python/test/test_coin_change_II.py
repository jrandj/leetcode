from src.coin_change_II import Solution

import unittest


class Tests(unittest.TestCase):
    def test_1(self):
        test_result = 4
        amount = 5
        coins = [1, 2, 5]
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.change(amount, coins))

    def test_2(self):
        test_result = 0
        amount = 3
        coins = [2]
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.change(amount, coins))

    def test_3(self):
        test_result = 1
        amount = 10
        coins = [10]
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.change(amount, coins))

    def test_4(self):
        test_result = 12701
        amount = 500
        coins = [1, 2, 5]
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.change(amount, coins))


if __name__ == "__main__":
    unittest.main()
