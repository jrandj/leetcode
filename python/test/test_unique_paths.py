import unittest

from src.unique_paths import Solution


class Tests(unittest.TestCase):
    def test_1a(self):
        test_result = 28
        m = 3
        n = 7
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.uniquePaths_recursive(m, n))

    def test_2a(self):
        test_result = 3
        m = 3
        n = 2
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.uniquePaths_recursive(m, n))

    def test_1b(self):
        test_result = 28
        m = 3
        n = 7
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.uniquePaths_iterative(m, n))

    def test_2b(self):
        test_result = 3
        m = 3
        n = 2
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.uniquePaths_iterative(m, n))


if __name__ == '__main__':
    unittest.main()
