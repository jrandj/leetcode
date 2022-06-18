import unittest
from src.implement_queue_using_stacks import MyQueue


class Tests(unittest.TestCase):
    def test_a1(self):
        test_result = True
        actual_result = MyQueue()
        actual_result.push(1)
        actual_result.push(2)
        actual_result.peek()
        actual_result.pop()
        actual_result.pop()
        self.assertEqual(test_result, actual_result.empty())


if __name__ == '__main__':
    unittest.main()
