from src.number_of_islands import Solution

import unittest


class Tests(unittest.TestCase):
    def test_1(self):
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]
        test_result = 1
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.numIslands(grid))

    def test_2(self):
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
        test_result = 3
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.numIslands(grid))


if __name__ == "__main__":
    unittest.main()
