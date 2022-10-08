from typing import List


class Solution:
    """
    You are a professional robber planning to rob houses along a street. Each house has a certain amount of money
    stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems
    connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

    Given an integer array nums representing the amount of money of each house, return the maximum amount of money you
    can rob tonight without alerting the police.
    """

    def rob_recursive(self, nums: List[int]) -> int:
        """
        Given an integer array nums representing the amount of money of each house, return the maximum amount of money you
        can rob tonight without alerting the police. This is the recursive solution.

        :param nums: The integer array representing the amount of money in each house.
        :type nums: List[int].
        :return: The maximum amount of money can you rob tonight.
        :rtype: Int.

        The time complexity is O(N) as we iterate through nums. Solution not accepted due to time limit exceeded.

        The space complexity is O(N) for the memoization array and recursion stack. Solution not accepted due to time
        limit exceeded.
        """
        memo = [None] * (len(nums) + 1)
        return self.helper(nums, len(nums) - 1, memo)

    def helper(self, nums: List[int], i: int, memo: List[int]) -> int:
        """
        A helper method for recursion.

        :param nums: The integer array representing the amount of money in each house.
        :type nums: List[int].
        :param i: The current index in nums.
        :type i: Int.
        :param memo: A memoization array.
        :type memo: List[int].
        :return: The maximum amount that can be robbed up to a particular index.
        :rtype: Int.
        """
        # base case
        if i < 0:
            return 0

        # check the memoization array first
        if memo[i]:
            result = memo[i]
        else:
            # we can rob the current house and get i - 2 or do not rob and get i - 1
            result = max(self.helper(nums, i - 2, memo) + nums[i], self.helper(nums, i - 1, memo))
            memo[i] = result

        return result

    @staticmethod
    def rob_iterative(nums: List[int]) -> int:
        """
        Given an integer array nums representing the amount of money of each house, return the maximum amount of money you
        can rob tonight without alerting the police. This is the iterative solution.

        :param nums: The integer array representing the amount of money in each house.
        :type nums: List[int].
        :return: The maximum amount that can be robbed up to a particular index.
        :rtype: Int.

        The time complexity is O(N) as we iterate through nums. Faster than 32.33% of solutions.

        The space complexity is constant as we don't use any additional data structures. Less memory than 65.29% of
        solutions.
        """
        if not nums:
            return 0

        # order is prev2, prev1, num
        prev1, prev2 = 0, 0

        for num in nums:
            # we can rob the current house and get i - 2 or do not rob and get i - 1
            tmp = max(prev2 + num, prev1)
            # move the pointers forward
            prev2 = prev1
            prev1 = tmp

        return tmp
