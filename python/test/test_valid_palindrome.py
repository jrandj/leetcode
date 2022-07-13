import unittest
from src.valid_palindrome import Solution


class Tests(unittest.TestCase):
    def test_a1(self):
        s = "A man, a plan, a canal: Panama"
        test_result = True
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.isPalindrome(s))

    def test_a2(self):
        s = "race a car"
        test_result = False
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.isPalindrome(s))

    def test_a3(self):
        s = " "
        test_result = True
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.isPalindrome(s))

    def test_a4(self):
        s = ".,"
        test_result = True
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.isPalindrome(s))


if __name__ == "__main__":
    unittest.main()
