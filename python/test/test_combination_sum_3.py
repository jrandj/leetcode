import unittest
from src.combination_sum_3 import Solution


class Tests(unittest.TestCase):
    def test_a1(self):
        k = 3
        n = 7
        TestSolution = Solution()
        actual_result = TestSolution.combinationSum3(k, n)
        test_result = [[1, 2, 4]]
        self.assertEqual(test_result, actual_result)

    def test_a2(self):
        k = 3
        n = 9
        TestSolution = Solution()
        actual_result = TestSolution.combinationSum3(k, n)
        test_result = [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
        self.assertEqual(test_result, actual_result)

    def test_a3(self):
        k = 4
        n = 1
        TestSolution = Solution()
        actual_result = TestSolution.combinationSum3(k, n)
        test_result = []
        self.assertEqual(test_result, actual_result)


if __name__ == '__main__':
    unittest.main()
