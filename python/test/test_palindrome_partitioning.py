from src.palindrome_partitioning import Solution
import unittest


class Tests(unittest.TestCase):
    def test_1(self):
        s = "aab"
        test_result = [["a", "a", "b"], ["aa", "b"]]
        actual_result = Solution()
        self.assertCountEqual(test_result, actual_result.partition(s))

    def test_2(self):
        s = "a"
        test_result = [["a"]]
        actual_result = Solution()
        self.assertCountEqual(test_result, actual_result.partition(s))


if __name__ == '__main__':
    unittest.main()
