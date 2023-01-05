import unittest

from src.daily_temperatures import Solution


class Tests(unittest.TestCase):
    def test_1(self):
        temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
        test_result = [1, 1, 4, 2, 1, 1, 0, 0]
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.dailyTemperatures(temperatures))

    def test_2(self):
        temperatures = [30, 40, 50, 60]
        test_result = [1, 1, 1, 0]
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.dailyTemperatures(temperatures))

    def test_3(self):
        temperatures = [30, 60, 90]
        test_result = [1, 1, 0]
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.dailyTemperatures(temperatures))


if __name__ == "__main__":
    unittest.main()
