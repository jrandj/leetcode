from typing import List
import sys


class Solution:
    """
    Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product,
    and return the product.

    The test cases are generated so that the answer will fit in a 32-bit integer.

    A subarray is a contiguous subsequence of the array.
    """

    def __init__(self):
        """
        Initialise the solution.
        """
        self.global_max = -sys.maxsize - 1

    def maxProduct_naive(self, nums: List[int]) -> int:
        """
        Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product,
        and return the product.

        :param nums: The integer input array nums.
        :type nums: List[Int].
        :return: The maximum product of any contiguous non-empty subarray.
        :rtype: Int.

        This is the brute force approach.

        The time complexity is O(N^2) for the 2 nested for loops. Exceeds the time limit.

        The space complexity is O(1) as we don't use any additional data structures.
        """
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        candidate = -sys.maxsize - 1
        for i in range(0, len(nums)):
            cum_sum = nums[i]
            candidate = max(candidate, cum_sum)
            for j in range(i + 1, len(nums)):
                cum_sum *= nums[j]
                candidate = max(candidate, cum_sum)

        return candidate

    def maxProduct_dynamic(self, nums: List[int]) -> int:
        """
        Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product,
        and return the product.

        :param nums: The integer input array nums.
        :type nums: List[Int].
        :return: The maximum product of any contiguous non-empty subarray.
        :rtype: Int.

        The time complexity is O(N) for the single loop. Faster than 84.56% of solutions.

        The space complexity is O(1) as we don't use any additional data structures. Less memory than 98.82% of
        solutions.
        """
        cur_min = cur_max = res = nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            # cur_min could become a candidate if n is negative!
            candidates = n, cur_max * n, cur_min * n
            cur_max = max(candidates)
            cur_min = min(candidates)
            res = max(res, cur_max)

        return res
