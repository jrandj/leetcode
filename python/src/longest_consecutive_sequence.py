from typing import List


class Solution:
    """
    Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

    You must write an algorithm that runs in O(n) time.
    """

    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

        :param nums: The unsorted array of integers.
        :type nums: List[Int].
        :return: The length of the longest consecutive sequence.
        :rtype: Int.

        The time complexity is O(N) as we iterate through nums twice. Faster than 97.13% of solutions.

        The space complexity is O(N) for the set. Less memory than 63.6% of solutions.
        """
        num_set = set(nums)
        longest = 0

        for n in num_set:
            # find starting elements
            if (n - 1) not in num_set:
                length = 0
                while (n + length) in num_set:
                    length += 1
                longest = max(longest, length)

        return longest
