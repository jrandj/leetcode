import unittest

from src.gas_station import Solution


class Tests(unittest.TestCase):
    def test_1a(self):
        gas = [1, 2, 3, 4, 5]
        cost = [3, 4, 5, 1, 2]
        test_result = 3
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.canCompleteCircuit_naive(gas, cost))

    def test_2a(self):
        gas = [2, 3, 4]
        cost = [3, 4, 3]
        test_result = -1
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.canCompleteCircuit_naive(gas, cost))

    def test_1b(self):
        gas = [1, 2, 3, 4, 5]
        cost = [3, 4, 5, 1, 2]
        test_result = 3
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.canCompleteCircuit_greedy(gas, cost))

    def test_2b(self):
        gas = [2, 3, 4]
        cost = [3, 4, 3]
        test_result = -1
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.canCompleteCircuit_greedy(gas, cost))


if __name__ == "__main__":
    unittest.main()
