from typing import List


def is_palindrome(s: str, l: int, r: int):
    """
    A helper method to check if the string s[l:r] is a palindrome.

    :param s: The string.
    :type s: Str.
    :param l: The left index of the string.
    :type l: Int.
    :param r: The right index of the string.
    :type r: Int.
    :return: True if s[l:r] is a palindrome, and False otherwise.
    :rtype: Bool.
    """
    while l < r:
        if s[l] != s[r]:
            return False
        l, r = l + 1, r - 1
    return True


class Solution:
    """
    Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible
    palindrome partitioning of s.

    A palindrome string is a string that reads the same backward as forward.
    """

    def __init__(self):
        """
        Initialise the solution.
        """
        self.res = []
        self.part = []

    def partition(self, s: str) -> List[List[str]]:
        """
        Return all possible palindrome partitioning of s.

        The time complexity is O(N*2^N) where N is the length of S, as it takes O(N) to determine if a substring is a
        palindrome or not. Faster than 5.01% of solutions.

        The space complexity is O(N) for the recursion stack. Less memory than 78.61% of solutions.

        :param s: The string.
        :type s: Str.
        :return: The list of partitions.
        :rtype: List[List[Str]].
        """
        self.dfs(0, s)
        return self.res

    def dfs(self, i: int, s: str):
        """
        A helper method to perform a Depth-First Search (DFS).

        :param i: The current index.
        :type i: Int.
        :param s: The string.
        :type s: Str.
        :return: NoneType.
        :rtype: NoneType.
        """
        # base case
        if i >= len(s):
            self.res.append(self.part.copy())
            return

        for j in range(i, len(s)):
            if is_palindrome(s, i, j):
                self.part.append(s[i:j + 1])
                self.dfs(j + 1, s)
                self.part.pop()
