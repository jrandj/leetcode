import unittest
from src.kth_largest_element_in_a_stream import Solution


class Tests(unittest.TestCase):

    def test_1a(self):
        test_result = 8
        kthLargest = Solution(3, [4, 5, 8, 2])
        kthLargest.add(3)
        kthLargest.add(5)
        kthLargest.add(10)
        kthLargest.add(9)
        actual_result = kthLargest.add(4)
        self.assertEqual(test_result, actual_result)


if __name__ == '__main__':
    unittest.main()
