class Solution:
    """
    Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

    An interleaving of two strings s and t is a configuration where s and t are divided into n and m substrings
    respectively, such that:

    s = s1 + s2 + ... + sn
    t = t1 + t2 + ... + tm
    |n - m| <= 1
    The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...

    Note: a + b is the concatenation of strings a and b.
    """

    def __init__(self):
        """
        Initialise the solution.
        """
        self.memo = None

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
        :param s1: The first string.
        :type s1: Str.
        :param s2: The second string.
        :type s2: Str.
        :param s3: The third string.
        :type s3: Str.
        :return: True if s3 is formed by interleaving s1 and s2, and False otherwise.
        :rtype: Bool.

        The time complexity is O(M*N) where M is the length of s1 and N is the length of s2. Faster than 90.91% of
        solutions.

        The space complexity is O(M*N) for the recursion stack and the memoization cache. Less memory than 28.10% of
        solutions.
        """
        self.memo = {}
        if len(s1) + len(s2) != len(s3):
            return False
        if len(s1) == 0:
            return s2 == s3
        if len(s2) == 0:
            return s1 == s3
        return self.dfs(s1, s2, s3, 0, 0, 0)

    def dfs(self, s1: str, s2: str, s3: str, i1: int, i2: int, i3: int) -> bool:
        """
        A helper method to perform a Depth-First Search (DFS).

        :param s1: The first string.
        :type s1: Str.
        :param s2: The second string.
        :type s2: Str.
        :param s3: The third string.
        :type s3: Str.
        :param i1: The current index of s1.
        :type i1: Int.
        :param i2: The current index of s2.
        :type i2: Int.
        :param i3: The current index of s3.
        :type i3: Int.
        :return: True if s3 is formed by interleaving s1 and s2 up to i3, and False otherwise.
        :rtype: Bool.
        """
        if i3 == len(s3) and i1 == len(s1) and i2 == len(s2):
            return True

        choose1, choose2 = False, False

        if (i1, i2) in self.memo:
            return self.memo[(i1, i2)]

        if i1 < len(s1) and i3 < len(s3) and s1[i1] == s3[i3]:
            choose1 = self.dfs(s1, s2, s3, i1 + 1, i2, i3 + 1)

        if i2 < len(s2) and i3 < len(s3) and s2[i2] == s3[i3]:
            choose2 = self.dfs(s1, s2, s3, i1, i2 + 1, i3 + 1)

        self.memo[(i1, i2)] = choose1 or choose2
        return self.memo[(i1, i2)]
