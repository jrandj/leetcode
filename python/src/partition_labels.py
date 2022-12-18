from typing import List


class Solution:
    """
    You are given a string s. We want to partition the string into as many parts as possible so that each letter
    appears in at most one part.

    Note that the partition is done so that after concatenating all the parts in order, the resultant string
    should be s.

    Return a list of integers representing the size of these parts.
    """

    def partitionLabels(self, s: str) -> List[int]:
        """
        You are given a string s. We want to partition the string into as many parts as possible so that each letter
        appears in at most one part. Return a list of integers representing the size of these parts.

        :param s: The input string.
        :type s: Str.
        :return: The list of integers representing the size of the partitions.
        :rtype: List[Int].

        The time complexity is O(N) as we iterate through s twice. Faster than 94.64% of solutions.

        The space complexity is O(26) which is O(1) for the hashmap. Less memory than 68.68% of solutions.
        """
        last_char = {}
        for i, c in enumerate(s):
            last_char[c] = i

        res = []
        size, end = 0, 0
        for i, c in enumerate(s):
            end = max(end, last_char[c])
            size += 1
            if i == end:
                res.append(size)
                size = 0

        return res
