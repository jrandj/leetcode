from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the
         elements of nums except nums[i].

        The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

        You must write an algorithm that runs in O(n) time and without using the division operation.

        :param nums: The input list.
        :return List[List[int]: The output list.

        The time complexity is O(N) as we iterate through nums twice. Faster than 44.36% of solutions.

        The space complexity is O(1) as we don't use any additional memory. Less memory than 80.80% of solutions.
        """
        res = [1] * len(nums)

        prefix, postfix = 1, 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
