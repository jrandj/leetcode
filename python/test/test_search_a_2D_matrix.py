import unittest
from src import search_a_2D_matrix


class Test(unittest.TestCase):
    def test_1(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 3
        actual_result = search_a_2D_matrix.Solution()
        self.assertTrue(actual_result.searchMatrix(matrix, target))

    def test_2(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 13
        actual_result = search_a_2D_matrix.Solution()
        self.assertFalse(actual_result.searchMatrix(matrix, target))


if __name__ == '__main__':
    unittest.main()
