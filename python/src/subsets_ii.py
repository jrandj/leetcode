from typing import List


class Solution:
    """
    Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

    The solution set must not contain duplicate subsets. Return the solution in any order.
    """

    def __init__(self):
        self.res = None

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

        :param nums: The input integer array.
        :type nums: List[int].
        :return: All possible subsets without duplicates.
        :rtype: List[List[int]].

        The time complexity is O(N*2^N). Faster than 49.36% of solutions.

        The space complexity is O(N) due to the recursive program stack. Less memory than 10.45% of solutions.
        """
        self.res = []
        nums.sort()
        self.dfs(0, [], nums)
        return self.res

    def dfs(self, i: int, subset: List[int], nums: List[int]):
        """
        A helper method to perform a Depth-First Search (DFS).

        :param i: The current index.
        :type i: Int.
        :param subset: The current subset.
        :type subset: List[int].
        :param nums: The input integer array.
        :type nums: List[int].
        :return: NoneType.
        :rtype: NoneType.
        """
        # base case
        if i >= len(nums):
            self.res.append(subset.copy())
            return

        # decision to include nums[i]
        subset.append(nums[i])
        self.dfs(i + 1, subset, nums)

        # decision to NOT include nums[i]
        subset.pop()
        # skip over duplicates
        while i + 1 < len(nums) and nums[i + 1] == nums[i]:
            i += 1
        self.dfs(i + 1, subset, nums)
