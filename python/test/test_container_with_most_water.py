import unittest
from src.container_with_most_water import Solution


class Tests(unittest.TestCase):
    def test_a1(self):
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        actual_result = Solution.maxArea(self, height)
        test_result = 49
        self.assertEqual(test_result, actual_result)

    def test_a2(self):
        height = [1, 1]
        actual_result = Solution.maxArea(self, height)
        test_result = 1
        self.assertEqual(test_result, actual_result)


if __name__ == '__main__':
    unittest.main()
