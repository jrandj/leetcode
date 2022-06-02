import unittest
from src.contains_duplicate import Solution


class Tests(unittest.TestCase):
    def test_1a(self):
        nums = [1, 2, 3, 1]
        actual_result = Solution.containsDuplicate_a(self, nums)
        test_result = True
        self.assertEqual(test_result, actual_result)

    def test_2a(self):
        nums = [1, 2, 3, 4]
        actual_result = Solution.containsDuplicate_a(self, nums)
        test_result = False
        self.assertEqual(test_result, actual_result)

    def test_3a(self):
        nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
        actual_result = Solution.containsDuplicate_a(self, nums)
        test_result = True
        self.assertEqual(test_result, actual_result)

    def test_1b(self):
        nums = [1, 2, 3, 1]
        actual_result = Solution.containsDuplicate_b(self, nums)
        test_result = True
        self.assertEqual(test_result, actual_result)

    def test_2b(self):
        nums = [1, 2, 3, 4]
        actual_result = Solution.containsDuplicate_b(self, nums)
        test_result = False
        self.assertEqual(test_result, actual_result)

    def test_3b(self):
        nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
        actual_result = Solution.containsDuplicate_b(self, nums)
        test_result = True
        self.assertEqual(test_result, actual_result)


if __name__ == '__main__':
    unittest.main()
