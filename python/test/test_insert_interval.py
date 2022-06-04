import unittest
from src.insert_interval import Solution


class Tests(unittest.TestCase):
    def test_a1(self):
        intervals = [[1, 3], [6, 9]]
        newInterval = [2, 5]
        actual_result = Solution.insert(self, intervals, newInterval)
        test_result = [[1, 5], [6, 9]]
        self.assertEqual(test_result, actual_result)

    def test_a2(self):
        intervals = [[1, 2], [5, 6]]
        newInterval = [3, 4]
        actual_result = Solution.insert(self, intervals, newInterval)
        test_result = [[1, 2], [3, 4], [5, 6]]
        self.assertEqual(test_result, actual_result)

    def test_a3(self):
        intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
        newInterval = [4, 8]
        actual_result = Solution.insert(self, intervals, newInterval)
        test_result = [[1, 2], [3, 10], [12, 16]]
        self.assertEqual(test_result, actual_result)


if __name__ == '__main__':
    unittest.main()
