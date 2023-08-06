import unittest
from src.task_scheduler import Solution


class Tests(unittest.TestCase):
    def test_1(self):
        tasks = ["A", "A", "A", "B", "B", "B"]
        n = 2
        test_result = 8
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.leastInterval(tasks, n))

    def test_2(self):
        tasks = ["A", "A", "A", "B", "B", "B"]
        n = 0
        test_result = 6
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.leastInterval(tasks, n))

    def test_3(self):
        tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
        n = 2
        test_result = 16
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.leastInterval(tasks, n))


if __name__ == "__main__":
    unittest.main()
