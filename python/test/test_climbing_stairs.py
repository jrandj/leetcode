import unittest
from src.climbing_stairs import Solution


class Tests(unittest.TestCase):

    def test_1(self):
        n = 2
        test_result = 2
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.climbStairs(n))

    def test_2(self):
        n = 3
        test_result = 3
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.climbStairs(n))


if __name__ == '__main__':
    unittest.main()
