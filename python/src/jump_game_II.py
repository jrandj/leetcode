import functools

import sys
from typing import List


class Solution:
    """
    You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

    Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at
    nums[i], you can jump to any nums[i + j] where:
        - 0 <= j <= nums[i] and
        - i + j < n

    Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach
    nums[n - 1].
    """

    def __init__(self):
        """
        Initialise the solution.
        """
        self.nums = None

    def jump_greedy(self, nums: List[int]) -> int:
        """
        Return the minimum number of jumps to reach nums[n - 1].

        :param nums: The input array.
        :type nums: List[Int].
        :return: The minimum number of jumps to reach nums[n - 1].
        :rtype: Int.

        The time complexity is O(N). Faster than 40.52% of solutions.

        The space complexity is O(1). Less memory than 56.92% of solutions.
        """
        # the initial range (after 0th jump) is [0,0]
        l = r = 0
        nJumps = 0
        while r < len(nums) - 1:
            nJumps += 1
            furthest = 0
            for i in range(l, r + 1):
                furthest = max(furthest, i + nums[i])
            l, r = r + 1, furthest

        return nJumps

    def jump_memoization(self, nums: List[int]) -> int:
        """
        Return the minimum number of jumps to reach nums[n - 1].

        :param nums: The input array.
        :type nums: List[Int].
        :return: The minimum number of jumps to reach nums[n - 1].
        :rtype: Int.

        The time complexity is O(N). Faster than 6.64% of solutions.

        The space complexity is O(N). Less memory than 5.01% of solutions.
        """
        self.nums = nums
        return self.min_jump(0)

    @functools.lru_cache(None)
    def min_jump(self, idx: int) -> int:
        """
        A helper method to calculate the minimum jumps.

        :param idx: The current index.
        :type idx: Int.
        :return: The number of jumps from this index.
        :rtype: Int.
        """
        if idx == len(self.nums) - 1:
            return 0
        elif self.nums[idx] >= len(self.nums) - idx - 1:
            return 1
        elif self.nums[idx] == 0:
            return sys.maxsize
        return 1 + min([self.min_jump(i) for i in range(idx + 1, idx + self.nums[idx] + 1)])
