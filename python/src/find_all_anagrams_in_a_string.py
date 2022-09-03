from typing import List


class Solution:
    """
    Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer
    in any order.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all
    the original letters exactly once.
    """

    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        Given two strings s and p, return an array of all the start indices of p's anagrams in s.

        :param s: The string that will anagrams will be searched for in.
        :type s: Str.
        :param p: The string used to generate anagrams to find in s.
        :type p: Str.
        :return: A list of the starting indices.
        :rtype: List[int]

        The time complexity seems like O(s*p), but is actually O(s) if you consider that p can only be length 26 as
        it is limited to characters a-z. Faster than 78.72% of solutions.

        The space complexity is O(1) as the dicts contain up to 26 entries only. Less memory than 79.79% of solutions.
        """
        # in this scenario we have no anagrams
        if len(p) > len(s):
            return []

        # build the characters for the substring starting at p[0]
        p_count, s_count = {}, {}
        for i in range(len(p)):
            p_count[p[i]] = p_count.get(p[i], 0) + 1
            s_count[s[i]] = s_count.get(s[i], 0) + 1

        # initialise the result with any anagram found at p[0]
        if p_count == s_count:
            res = [0]
        else:
            res = []

        # look at the remaining characters in p
        l = 0
        for r in range(len(p), len(s)):
            # keep dict up to date with characters in the window
            s_count[s[r]] = s_count.get(s[r], 0) + 1
            s_count[s[l]] -= 1

            # need to remove s[l] completely if it has no more elements
            if s_count[s[l]] == 0:
                s_count.pop(s[l])

            l += 1

            # add any new result
            if s_count == p_count:
                res.append(l)

        return res
