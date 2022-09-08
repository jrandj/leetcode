import unittest
from src.time_based_key_value_store import TimeMap


class Tests(unittest.TestCase):
    def test_1(self):
        actual_result = TimeMap()
        actual_result.set("foo", "bar", 1)
        self.assertEqual("bar", actual_result.get("foo", 1))
        actual_result.get("foo", 3)
        actual_result.set("foo", "bar2", 4)
        self.assertEqual("bar2", actual_result.get("foo", 4))
        self.assertEqual("bar2", actual_result.get("foo", 5))


if __name__ == "__main__":
    unittest.main()
