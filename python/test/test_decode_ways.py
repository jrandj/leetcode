from src.decode_ways import Solution

import unittest


class Tests(unittest.TestCase):
    def test_1(self):
        s = "12"
        test_result = 2
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.numDecodings(s))

    def test_2(self):
        s = "226"
        test_result = 3
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.numDecodings(s))

    def test_3(self):
        s = "06"
        test_result = 0
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.numDecodings(s))


if __name__ == "__main__":
    unittest.main()
