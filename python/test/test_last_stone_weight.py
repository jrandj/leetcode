import unittest

from src.last_stone_weight import Solution


class Tests(unittest.TestCase):

    def test_1(self):
        stones = [2, 7, 4, 1, 8, 1]
        test_result = 1
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.lastStoneWeight(stones))

    def test_2(self):
        stones = [1]
        test_result = 1
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.lastStoneWeight(stones))

    def test_3(self):
        stones = [3, 7, 2]
        test_result = 2
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.lastStoneWeight(stones))


if __name__ == '__main__':
    unittest.main()
