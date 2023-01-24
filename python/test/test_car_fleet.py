import unittest

from src.car_fleet import Solution


class Tests(unittest.TestCase):
    def test_1(self):
        target = 12
        position = [10, 8, 0, 5, 3]
        speed = [2, 4, 1, 1, 3]
        test_result = 3
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.carFleet(target, position, speed))

    def test_2(self):
        target = 10
        position = [3]
        speed = [3]
        test_result = 1
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.carFleet(target, position, speed))

    def test_3(self):
        target = 100
        position = [0, 2, 4]
        speed = [4, 2, 1]
        test_result = 1
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.carFleet(target, position, speed))


if __name__ == "__main__":
    unittest.main()
