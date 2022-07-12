import unittest
from src.LRU_cache import LRUCache


class Tests(unittest.TestCase):
    def test_a1(self):
        actual_result = LRUCache(2)
        actual_result.put(1, 1)
        actual_result.put(2, 2)
        self.assertEqual(actual_result.get(1), 1)
        actual_result.put(3, 3)
        self.assertEqual(actual_result.get(2), -1)
        actual_result.put(4, 4)
        self.assertEqual(actual_result.get(1), -1)
        self.assertEqual(actual_result.get(3), 3)
        self.assertEqual(actual_result.get(4), 4)


if __name__ == '__main__':
    unittest.main()
