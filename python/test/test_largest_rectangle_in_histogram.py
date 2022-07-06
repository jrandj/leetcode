import unittest
from src.largest_rectangle_in_histogram import Solution


class Tests(unittest.TestCase):
    def test_a1(self):
        heights = [2, 1, 5, 6, 2, 3]
        test_result = 10
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.largestRectangleArea(heights))

    def test_a2(self):
        heights = [2, 4]
        test_result = 4
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.largestRectangleArea(heights))


if __name__ == '__main__':
    unittest.main()
