import unittest

from src.encode_and_decode_strings import Solution


class Tests(unittest.TestCase):
    def test1(self):
        s = ["lint", "code", "love", "you"]
        test_result = ["lint", "code", "love", "you"]
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.decode(actual_result.encode(s)))


if __name__ == "__main__":
    unittest.main()
