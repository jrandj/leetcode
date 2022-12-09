import unittest

from src.jump_game_II import Solution


class Tests(unittest.TestCase):
    def test_1a(self):
        nums = [2, 3, 1, 1, 4]
        test_result = 2
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.jump_memoization(nums))

    def test_2a(self):
        nums = [2, 3, 0, 1, 4]
        test_result = 2
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.jump_memoization(nums))

    def test_1b(self):
        nums = [2, 3, 1, 1, 4]
        test_result = 2
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.jump_greedy(nums))

    def test_2b(self):
        nums = [2, 3, 0, 1, 4]
        test_result = 2
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.jump_greedy(nums))


if __name__ == "__main__":
    unittest.main()
