import unittest

from src.koko_eating_bananas import Solution


class Tests(unittest.TestCase):
    def test_1(self):
        piles = [3, 6, 7, 11]
        h = 8
        actual_result = Solution()
        test_result = 4
        self.assertEqual(test_result, actual_result.minEatingSpeed(piles, h))

    def test_2(self):
        piles = [30, 11, 23, 4, 20]
        h = 5
        actual_result = Solution()
        test_result = 30
        self.assertEqual(test_result, actual_result.minEatingSpeed(piles, h))

    def test_3(self):
        piles = [30, 11, 23, 4, 20]
        h = 6
        actual_result = Solution()
        test_result = 23
        self.assertEqual(test_result, actual_result.minEatingSpeed(piles, h))


if __name__ == "__main__":
    unittest.main()
