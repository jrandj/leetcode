import unittest

from src.find_the_duplicate_number import Solution


class Tests(unittest.TestCase):
    def test_1(self):
        nums = [1, 3, 4, 2, 2]
        test_result = 2
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.findDuplicate(nums))

    def test_2(self):
        nums = [3, 1, 3, 4, 2]
        test_result = 3
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.findDuplicate(nums))


if __name__ == "__main__":
    unittest.main()
