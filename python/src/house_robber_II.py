from typing import List


class Solution:
    """
    You are a professional robber planning to rob houses along a street. Each house has a certain amount of money
    stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last
    one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if
    two adjacent houses were broken into on the same night.

    Given an integer array nums representing the amount of money of each house, return the maximum amount of money you
    can rob tonight without alerting the police.
    """

    def rob(self, nums: List[int]) -> int:
        """
        Return the maximum amount of money you can rob tonight without alerting the police.

        :param nums: The input array.
        :type nums: List[Int].
        :return: The maximum you can rob.
        :rtype: Int.

        The time complexity is O(N) as we iterate through nums. Faster than 14.25% of solutions.

        The space complexity is O(1) as we don't use any additional data structures. Less memory than 71.39% of
        solutions.
        """
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]

        all_except_first = nums[1:]
        all_except_last = nums[:-1]

        return max(self.helper(all_except_first), self.helper(all_except_last))

    def helper(self, nums: int):
        """
        A helper function for rob.

        :param nums: The input array.
        :type nums: List[Int].
        :return: The maximum you can rob.
        :rtype: Int.
        """
        # order is 2 1 0 prev1 prev2
        prev1, prev2 = 0, 0
        for num in nums:
            tmp = max(num + prev2, prev1)
            prev2 = prev1
            prev1 = tmp
        return tmp
