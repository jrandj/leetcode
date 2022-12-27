import unittest

from src.valid_parenthesis_string import Solution


class Tests(unittest.TestCase):
    def test_1a(self):
        actual_result = Solution()
        s = "()"
        self.assertTrue(actual_result.checkValidString(s))

    def test_2a(self):
        actual_result = Solution()
        s = "(*)"
        self.assertTrue(actual_result.checkValidString(s))

    def test_3a(self):
        actual_result = Solution()
        s = "(*))"
        self.assertTrue(actual_result.checkValidString(s))

    def test_4a(self):
        actual_result = Solution()
        s = "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"
        self.assertFalse(actual_result.checkValidString(s))

    def test_5a(self):
        actual_result = Solution()
        s = "((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"
        self.assertTrue(actual_result.checkValidString(s))

    def test_1b(self):
        actual_result = Solution()
        s = "()"
        self.assertTrue(actual_result.checkValidString_greedy(s))

    def test_2b(self):
        actual_result = Solution()
        s = "(*)"
        self.assertTrue(actual_result.checkValidString_greedy(s))

    def test_3b(self):
        actual_result = Solution()
        s = "(*))"
        self.assertTrue(actual_result.checkValidString_greedy(s))

    def test_4b(self):
        actual_result = Solution()
        s = "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"
        self.assertFalse(actual_result.checkValidString_greedy(s))

    def test_5b(self):
        actual_result = Solution()
        s = "((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"
        self.assertTrue(actual_result.checkValidString_greedy(s))


if __name__ == "__main__":
    unittest.main()
