from typing import List


class Solution:
    """
    Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two
    subsets such that the sum of elements in both subsets is equal.
    """

    def canPartition_recursive(self, nums: List[int]) -> bool:
        """
        Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two
        subsets such that the sum of elements in both subsets is equal.

        :param nums: The input array.
        :type nums: List[Int].
        :return: True if the nums can be partitioned, and False otherwise.
        :rtype: Bool.

        The time complexity is O(N*SUM(N)). Results in time limit exceeded.

        The space complexity is O(N*SUM(N)). Results in time limit exceeded.
        """
        all_sum = sum(nums)
        # an odd sum cannot have a partition
        if all_sum % 2 != 0:
            return False
        target = all_sum // 2
        memo = {}
        return self.dfs(nums, 0, target, memo)

    def dfs(self, nums: List[int], index: int, remaining: int, memo: dict):
        """
        A helper method to perform a Depth-First Search (DFS).

        :param nums: The input array.
        :type nums: List[Int].
        :param index: The current index in nums.
        :type index: Int.
        :param remaining: The remaining sum for the partition.
        :type remaining: Int.
        :param memo: The memoization dict.
        :type memo: Dict.
        :return: True if the subarray can be partitioned, and False otherwise.
        :rtype: Bool.
        """
        # base cases
        if index == len(nums) or remaining < 0:
            return False
        elif remaining == 0:
            return True

        # use cache
        key = (remaining, index)
        if memo.get(key, None):
            return memo[key]

        # choose and do not choose
        memo[key] = self.dfs(nums, index + 1, remaining - nums[index], memo) or \
                    self.dfs(nums, index + 1, remaining, memo)

        return memo[key]

    def canPartition_iterative(self, nums: List[int]) -> bool:
        """
        Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two
        subsets such that the sum of elements in both subsets is equal.

        :param nums: The input array.
        :type nums: List[Int].
        :return: True if the nums can be partitioned, and False otherwise.
        :rtype: Bool.

        The time complexity is O(N*SUM(N)). Faster than 43.00% of solutions.

        The space complexity is O(SUM(N)). Less memory than 91.20% of solutions.
        """
        all_sum = sum(nums)
        # an odd sum cannot have a partition
        if all_sum % 2 != 0:
            return False
        target = all_sum // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        return dp[-1]
