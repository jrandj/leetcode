from typing import List


class Solution:
    """
    Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could
    represent. Return the answer in any order.

    A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any
    letters.
    """

    def __init__(self):
        """
        Initialise the Solution.
        """
        self.res = []
        self.digits_to_chars = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jlk",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

    def letterCombinations(self, digits: str) -> List[str]:
        """
        Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number
        could represent.

        The time complexity is O(4^N) where N is the length of digits, as there are at most 4 choices per digit.
        Faster than 98.29% of solutions.

        The space complexity is O(N*4^N) as each string is of length N. Less memory than 79.23% of solutions.

        :param digits: A string containing digits from 2-9 inclusive.
        :type digits: Str.
        :return: all possible letter combinations that the number could represent.
        :rtype: Str.
        """
        if digits:
            self.dfs(0, digits, "")
        return self.res

    def dfs(self, i: int, digits: str, combination: str):
        """
        A helper function to perform a Depth-First Search (DFS).

        :param i: The current index.
        :type i: Int.
        :param digits: A string containing digits from 2-9 inclusive.
        :type digits: Str.
        :param combination: The current candidate combination.
        :type combination: Str.
        :return: NoneType.
        :rtype: NoneType.
        """
        # base case
        if len(combination) == len(digits):
            self.res.append(combination)
            return

        for c in self.digits_to_chars[digits[i]]:
            self.dfs(i + 1, digits, combination + c)
