import unittest
from src.trapping_rain_water import Solution


class Tests(unittest.TestCase):
    def test_a1(self):
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        actual_result = Solution.trap(self, height)
        test_result = 6
        self.assertEqual(test_result, actual_result)

    def test_a2(self):
        height = [4, 2, 0, 3, 2, 5]
        actual_result = Solution.trap(self, height)
        test_result = 9
        self.assertEqual(test_result, actual_result)


if __name__ == '__main__':
    unittest.main()
