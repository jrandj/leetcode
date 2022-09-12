import unittest
from src.maximum_profit_in_job_scheduling import Solution


class Tests(unittest.TestCase):
    def test_1(self):
        startTime = [1, 2, 3, 3]
        endTime = [3, 4, 5, 6]
        profit = [50, 10, 40, 70]
        test_result = 120
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.jobScheduling(startTime, endTime, profit))

    def test_2(self):
        startTime = [1, 2, 3, 4, 6]
        endTime = [3, 5, 10, 6, 9]
        profit = [20, 20, 100, 70, 60]
        test_result = 150
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.jobScheduling(startTime, endTime, profit))

    def test_3(self):
        startTime = [1, 1, 1]
        endTime = [2, 3, 4]
        profit = [5, 6, 4]
        test_result = 6
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.jobScheduling(startTime, endTime, profit))


if __name__ == '__main__':
    unittest.main()
