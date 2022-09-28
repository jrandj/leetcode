from src.house_robber import Solution
import unittest


class Tests(unittest.TestCase):
    def test_1a(self):
        nums = [1, 2, 3, 1]
        test_result = 4
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.rob_recursive(nums))

    def test_2a(self):
        nums = [2, 7, 9, 3, 1]
        test_result = 12
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.rob_recursive(nums))

    def test_3a(self):
        nums = [2, 1, 1, 2]
        test_result = 4
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.rob_recursive(nums))

    def test_1b(self):
        nums = [1, 2, 3, 1]
        test_result = 4
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.rob_iterative(nums))

    def test_2b(self):
        nums = [2, 7, 9, 3, 1]
        test_result = 12
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.rob_iterative(nums))

    def test_3b(self):
        nums = [2, 1, 1, 2]
        test_result = 4
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.rob_iterative(nums))


if __name__ == '__main__':
    unittest.main()
