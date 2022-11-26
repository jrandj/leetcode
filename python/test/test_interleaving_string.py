from src.interleaving_string import Solution

import unittest


class Tests(unittest.TestCase):
    def test_1(self):
        s1 = "aabcc"
        s2 = "dbbca"
        s3 = "aadbbcbcac"
        actual_result = Solution()
        self.assertTrue(actual_result.isInterleave(s1, s2, s3))

    def test_2(self):
        s1 = "aabcc"
        s2 = "dbbca"
        s3 = "aadbbbaccc"
        actual_result = Solution()
        self.assertFalse(actual_result.isInterleave(s1, s2, s3))

    def test_3(self):
        s1 = ""
        s2 = ""
        s3 = ""
        actual_result = Solution()
        self.assertTrue(actual_result.isInterleave(s1, s2, s3))

    def test_4(self):
        s1 = "aabcc"
        s2 = "dbbca"
        s3 = "aadbbcbcac"
        actual_result = Solution()
        self.assertTrue(actual_result.isInterleave(s1, s2, s3))

    def test_5(self):
        s1 = "a"
        s2 = "b"
        s3 = "a"
        actual_result = Solution()
        self.assertFalse(actual_result.isInterleave(s1, s2, s3))

    def test_6(self):
        s1 = ""
        s2 = ""
        s3 = "a"
        actual_result = Solution()
        self.assertFalse(actual_result.isInterleave(s1, s2, s3))


if __name__ == "__main__":
    unittest.main()
