class Solution:
    """
    Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

    In other words, return true if one of s1's permutations is the substring of s2.
    """

    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

        :param s1: The first string.
        :type s1: Str.
        :param s2: The second string.
        :type s2: Str.
        :return: True if s2 contains a permutation of s1, and False otherwise.
        :rtype: Boolean.

        The time complexity is O(N + M) to iterate through each string. Faster than 79.01% of solutions.

        The space complexity is O(N) for the counter for s1. Less memory than 66.57% of solutions.
        """
        s1_chars = {}
        w = len(s1)
        matched = 0

        # determine the counter for s1
        for c in s1:
            s1_chars[c] = 1 + s1_chars.get(c, 0)

        # slide a window over s2
        for i in range(len(s2)):
            if s2[i] in s1_chars:
                s1_chars[s2[i]] -= 1
                if s1_chars[s2[i]] == 0:
                    matched += 1

            # slide the window to the right by 1 if we haven't found a palindrome
            if i >= w and s2[i - w] in s1_chars:
                if s1_chars[s2[i - w]] == 0:
                    matched -= 1
                s1_chars[s2[i - w]] += 1

            # this is the definition of a palindrome
            if matched == len(s1_chars):
                return True

        return False
