import sys
from typing import List


class Solution:
    """
    Given an integer array nums, find the subarray which has the largest sum and return its sum.
    """

    def maxSubArray_naive(self, nums: List[int]) -> int:
        """
        Given an integer array nums, find the subarray which has the largest sum and return its sum.

        :param nums: The input integer array.
        :type nums: List[Int].
        :return: The largest sum associated with a subarray.
        :rtype: Int.

        The time complexity is O(N^2). Results in time limit exceeded.

        The space complexity is O(1) as we don't use any additional data structures. Results in time limit exceeded.
        """
        max_sum = -sys.maxsize - 1
        for i in range(len(nums)):
            current_max = 0
            for j in range(i, len(nums)):
                current_max += nums[j]
                max_sum = max(max_sum, current_max)
        return max_sum

    def maxSubArray_dp(self, nums: List[int]) -> int:
        """
        Given an integer array nums, find the subarray which has the largest sum and return its sum.

        :param nums: The input integer array.
        :type nums: List[Int].
        :return: The largest sum associated with a subarray.
        :rtype: Int.

        The time complexity is O(N). Faster than 71.35% of solutions.

        The space complexity is O(1) as we don't use any additional data structures. Less memory than 96.27% of
        solutions.
        """
        max_ending_here = nums[0]
        max_so_far = nums[0]
        for i in range(1, len(nums)):
            max_ending_here = max(nums[i], nums[i] + max_ending_here)
            max_so_far = max(max_so_far, max_ending_here)

        return max_so_far
