from typing import List


class Solution:
    """
    You are given an integer array nums and an integer target.

    You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums
    and then concatenate all the integers.

    For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the
    expression "+2-1".

    Return the number of different expressions that you can build, which evaluates to target.
    """

    def __init__(self):
        """
        Initialise the solution.
        """
        self.memo = None

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        Return the number of different expressions that you can build, which evaluates to target.

        :param nums: The input array.
        :type nums: List[Int].
        :param target: The target sum.
        :type target: Int.
        :return: The number of ways you can add to the target sum.
        :rtype: Int.

        The time complexity is O*(T*N) where N is the length of nums and T is the total of all elements in nums.
        Faster than 17.86% of solutions.

        The space complexity is O(N) for the recursion stack and memoization dict. Less memory than 58.32% of solutions.
        """
        self.memo = {}  # (index, total) -> # of ways
        return self.dfs(nums, 0, target, 0)

    def dfs(self, nums: List[int], total: int, target: int, index: int) -> int:
        """
        A helper method to perform a Depth-First Search (DFS).

        :param nums: The input array.
        :type nums: List[Int].
        :param total: The current total up to the index.
        :type total: Int.
        :param target: The target sum.
        :type target: Int.
        :param index: The current index.
        :type index: Int.
        :return: The number of ways you can add to the target sum.
        :rtype: Int.
        """
        # base case
        if index == len(nums):
            return 1 if total == target else 0
        if (index, total) in self.memo:
            return self.memo[(index, total)]

        self.memo[(index, total)] = self.dfs(nums, total - nums[index], target, index + 1) + \
                                    self.dfs(nums, total + nums[index], target, index + 1)
        return self.memo[(index, total)]
