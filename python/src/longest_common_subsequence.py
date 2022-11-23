class Solution:
    """
    Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common
    subsequence, return 0.

    A subsequence of a string is a new string generated from the original string with some characters (can be none)
    deleted without changing the relative order of the remaining characters.

    For example, "ace" is a subsequence of "abcde".

    A common subsequence of two strings is a subsequence that is common to both strings.
    """

    def __init__(self):
        """
        Initialise the solution.
        """
        self.memo = None

    def longestCommonSubsequence_recursion(self, text1: str, text2: str) -> int:
        """
        Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common
        subsequence, return 0.

        :param text1: The first string.
        :type text1: Str.
        :param text2: The second string.
        :type text2: Str.
        :return: The longest common subsequence.
        :rtype: Int.

        The time complexity is O(M*N). Faster than 7.70% of solutions.

        The space complexity is O(M*N). Less memory than 17.38% of solutions.
        """
        self.memo = {}
        return self.recursive_helper(text1, text2, 0, 0)

    def recursive_helper(self, text1: str, text2: str, i: int, j: int) -> int:
        """
        A helper method for recursion.

        :param text1: The first string.
        :type text1: Str.
        :param text2: The second string.
        :type text2: Str.
        :param i: The current index in the first string.
        :type i: Int.
        :param j: The current index in the second string.
        :type j: Int.
        :return: The longest common subsequence.
        :rtype: Int.
        """
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        if i == len(text1) or j == len(text2):
            res = 0
        elif text1[i] == text2[j]:
            res = 1 + self.recursive_helper(text1, text2, i + 1, j + 1)
        else:
            res = max(self.recursive_helper(text1, text2, i + 1, j), self.recursive_helper(text1, text2, i, j + 1))

        self.memo[(i, j)] = res
        return res

    def longestCommonSubsequence_dp(self, text1: str, text2: str) -> int:
        """
        Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common
        subsequence, return 0.

        :param text1: The first string.
        :type text1: Str.
        :param text2: The second string.
        :type text2: Str.
        :return: The longest common subsequence.
        :rtype: Int.

        The time complexity is O(M*N). Faster than 50.46% of solutions.

        The space complexity is O(M*N). Less memory than 80.23% of solutions.
        """
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for i in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]
