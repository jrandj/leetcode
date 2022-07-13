import unittest
from src.valid_anagram import Solution


class Tests(unittest.TestCase):

    def test_a1(self):
        s = "anagram"
        t = "nagaram"
        test_result = True
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.isAnagram(s, t))

    def test_a2(self):
        s = "rat"
        t = "car"
        test_result = False
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.isAnagram(s, t))

    def test_a3(self):
        s = "ab"
        t = "a"
        test_result = False
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.isAnagram(s, t))


if __name__ == "__main__":
    unittest.main()
