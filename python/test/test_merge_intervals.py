import unittest
from src.merge_intervals import Solution


class Tests(unittest.TestCase):
    def test_a1(self):
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        actual_result = Solution.merge(self, intervals)
        test_result = [[1, 6], [8, 10], [15, 18]]
        self.assertEqual(test_result, actual_result)

    def test_a2(self):
        intervals = [[1, 4], [4, 5]]
        actual_result = Solution.merge(self, intervals)
        test_result = [[1, 5]]
        self.assertEqual(test_result, actual_result)

    def test_a3(self):
        intervals = [[1, 3]]
        actual_result = Solution.merge(self, intervals)
        test_result = [[1, 3]]
        self.assertEqual(test_result, actual_result)

    def test_a4(self):
        intervals = [[1, 4], [5, 6]]
        actual_result = Solution.merge(self, intervals)
        test_result = [[1, 4], [5, 6]]
        self.assertEqual(test_result, actual_result)


if __name__ == '__main__':
    unittest.main()
