import unittest
from src.combination_sum import Solution


class Tests(unittest.TestCase):
    def test_a1(self):
        candidates = [2, 3, 6, 7]
        target = 7
        TestSolution = Solution()
        actual_result = TestSolution.combinationSum(candidates, target)
        test_result = [[2, 2, 3], [7]]
        self.assertEqual(test_result, actual_result)

    def test_a2(self):
        candidates = [2, 3, 5]
        target = 8
        TestSolution = Solution()
        actual_result = TestSolution.combinationSum(candidates, target)
        test_result = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        self.assertEqual(test_result, actual_result)

    def test_a3(self):
        candidates = [2]
        target = 1
        TestSolution = Solution()
        actual_result = TestSolution.combinationSum(candidates, target)
        test_result = []
        self.assertEqual(test_result, actual_result)


if __name__ == '__main__':
    unittest.main()
