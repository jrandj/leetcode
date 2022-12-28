from typing import List


class Solution:
    """
    Given an array of strings strs, group the anagrams together. You can return the answer in any order.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all
    the original letters exactly once.
    """

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Given an array of strings strs, group the anagrams together.

        :param strs: The input array of strings.
        :type strs: Str.
        :return: The list of grouped anagrams.
        :rtype: List[List[Str]].

        The time complexity is O(N*M) where N is the length of strs and M is the average length of a string in strs.
        Faster than 72.27% of solutions.

        The space complexity is O(N) where N is the length of strs. Less memory than 33.60% of solutions.
        """
        res = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1

            # we cannot use list as a key so convert to tuple
            if res.get(tuple(count), None):
                res[tuple(count)].append(s)
            else:
                res[tuple(count)] = [s]

        return list(res.values())
