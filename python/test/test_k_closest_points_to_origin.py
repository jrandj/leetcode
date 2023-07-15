import unittest

from src.k_closest_points_to_origin import Solution


class Test(unittest.TestCase):

    def test_1(self):
        points = [[1, 3], [-2, 2]]
        k = 1
        test_result = [[-2, 2]]
        actual_result = Solution()
        self.assertListEqual(test_result, actual_result.kClosest(points, k))

    def test_2(self):
        points = [[3, 3], [5, -1], [-2, 4]]
        k = 2
        test_result = [[3, 3], [-2, 4]]
        actual_result = Solution()
        self.assertListEqual(test_result, actual_result.kClosest(points, k))


if __name__ == "__main__":
    unittest.main()
