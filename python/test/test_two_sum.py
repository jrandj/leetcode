import unittest
from src.two_sum import Solution


class Tests(unittest.TestCase):
    def test_a1(self):
        nums = [2, 7, 11, 15]
        target = 9
        actual_result = Solution.two_sum_a(self, nums, target)
        test_result = [0, 1]
        self.assertEqual(test_result, actual_result)

    def test_a2(self):
        nums = [3, 2, 4]
        target = 6
        actual_result = Solution.two_sum_a(self, nums, target)
        test_result = [1, 2]
        self.assertEqual(test_result, actual_result)

    def test_a3(self):
        nums = [3, 3]
        target = 6
        actual_result = Solution.two_sum_a(self, nums, target)
        test_result = [0, 1]
        self.assertEqual(test_result, actual_result)

    def test_b1(self):
        nums = [2, 7, 11, 15]
        target = 9
        actual_result = Solution.two_sum_b(self, nums, target)
        test_result = [0, 1]
        self.assertEqual(test_result, actual_result)

    def test_b2(self):
        nums = [3, 2, 4]
        target = 6
        actual_result = Solution.two_sum_b(self, nums, target)
        test_result = [1, 2]
        self.assertEqual(test_result, actual_result)

    def test_b3(self):
        nums = [3, 3]
        target = 6
        actual_result = Solution.two_sum_b(self, nums, target)
        test_result = [0, 1]
        self.assertEqual(test_result, actual_result)


if __name__ == '__main__':
    unittest.main()
