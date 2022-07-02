import unittest
from src.min_stack import MinStack


class Tests(unittest.TestCase):
    def test_a1(self):
        actual_result = MinStack()
        actual_result.push(-2)
        actual_result.push(0)
        actual_result.push(-3)
        self.assertEqual(-3, actual_result.getMin())
        actual_result.pop()
        self.assertEqual(0, actual_result.top())
        self.assertEqual(-2, actual_result.getMin())


if __name__ == '__main__':
    unittest.main()
