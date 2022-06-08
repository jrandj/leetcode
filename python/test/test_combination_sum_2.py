import unittest
from src.combination_sum_2 import Solution


class Tests(unittest.TestCase):
    def test_a1(self):
        candidates = [10, 1, 2, 7, 6, 1, 5]
        target = 8
        TestSolution = Solution()
        actual_result = TestSolution.combinationSum2(candidates, target)
        test_result = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
        self.assertEqual(test_result, actual_result)

    def test_a2(self):
        candidates = [2, 5, 2, 1, 2]
        target = 5
        TestSolution = Solution()
        actual_result = TestSolution.combinationSum2(candidates, target)
        test_result = [[1, 2, 2], [5]]
        self.assertEqual(test_result, actual_result)


if __name__ == '__main__':
    unittest.main()
