import unittest
from src.majority_element import Solution


class Tests(unittest.TestCase):
    def test_a1(self):
        nums = [3, 2, 3]
        actual_result = Solution.majorityElement_a(self, nums)
        test_result = 3
        self.assertEqual(test_result, actual_result)

    def test_a2(self):
        nums = [2, 2, 1, 1, 1, 2, 2]
        actual_result = Solution.majorityElement_a(self, nums)
        test_result = 2
        self.assertEqual(test_result, actual_result)

    def test_a3(self):
        nums = [3, 3, 4]
        actual_result = Solution.majorityElement_a(self, nums)
        test_result = 3
        self.assertEqual(test_result, actual_result)

    def test_b1(self):
        nums = [3, 2, 3]
        actual_result = Solution.majorityElement_b(self, nums)
        test_result = 3
        self.assertEqual(test_result, actual_result)

    def test_b2(self):
        nums = [2, 2, 1, 1, 1, 2, 2]
        actual_result = Solution.majorityElement_b(self, nums)
        test_result = 2
        self.assertEqual(test_result, actual_result)

    def test_b3(self):
        nums = [3, 3, 4]
        actual_result = Solution.majorityElement_b(self, nums)
        test_result = 3
        self.assertEqual(test_result, actual_result)


if __name__ == '__main__':
    unittest.main()
