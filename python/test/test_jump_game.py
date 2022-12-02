import unittest

from src.jump_game import Solution


class Tests(unittest.TestCase):
    def test_1a(self):
        nums = [2, 3, 1, 1, 4]
        actual_result = Solution()
        self.assertTrue(actual_result.canJump_naive(nums))

    def test_2a(self):
        nums = [3, 2, 1, 0, 4]
        actual_result = Solution()
        self.assertFalse(actual_result.canJump_naive(nums))

    def test_3a(self):
        nums = [2, 0]
        actual_result = Solution()
        self.assertTrue(actual_result.canJump_naive(nums))

    def test_4a(self):
        nums = [2, 0, 0]
        actual_result = Solution()
        self.assertTrue(actual_result.canJump_naive(nums))

    def test_1b(self):
        nums = [2, 3, 1, 1, 4]
        actual_result = Solution()
        self.assertTrue(actual_result.canJump_memo(nums))

    def test_2b(self):
        nums = [3, 2, 1, 0, 4]
        actual_result = Solution()
        self.assertFalse(actual_result.canJump_memo(nums))

    def test_3b(self):
        nums = [2, 0]
        actual_result = Solution()
        self.assertTrue(actual_result.canJump_memo(nums))

    def test_4b(self):
        nums = [2, 0, 0]
        actual_result = Solution()
        self.assertTrue(actual_result.canJump_memo(nums))

    def test_1c(self):
        nums = [2, 3, 1, 1, 4]
        actual_result = Solution()
        self.assertTrue(actual_result.canJump_dfs(nums))

    def test_2c(self):
        nums = [3, 2, 1, 0, 4]
        actual_result = Solution()
        self.assertFalse(actual_result.canJump_dfs(nums))

    def test_3c(self):
        nums = [2, 0]
        actual_result = Solution()
        self.assertTrue(actual_result.canJump_dfs(nums))

    def test_4c(self):
        nums = [2, 0, 0]
        actual_result = Solution()
        self.assertTrue(actual_result.canJump_dfs(nums))


if __name__ == "__main__":
    unittest.main()
