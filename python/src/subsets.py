from typing import List


class Solution:
    """
    Given an integer array nums of unique elements, return all possible subsets (the power set).

    The solution set must not contain duplicate subsets. Return the solution in any order.
    """

    def __init__(self):
        """
        Initialise the Solution.
        """
        self.res = None

    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Given an integer array nums of unique elements, return all possible subsets (the power set).

        :param nums: The input array of unique elements.
        :type nums: List[int].
        :return: The subsets of nums.
        :rtype: List[List[int]].

        The time complexity is O(N*2^N) as we make a decision for each N. Faster than 97.90% of solutions.

        The space complexity is O(N) for the recursion stack. Less memory than 82.64% of solutions.
        """
        self.res = []
        self.dfs(0, [], nums)
        return self.res

    def dfs(self, i: int, subset: List[int], nums: List[int]):
        """
        A helper method to perform a depth-first search.

        :param i: The current index of nums.
        :type i: Int.
        :param subset: The current subset.
        :type subset: List[int].
        :param nums: The input array of unique elements.
        :type nums: List[int].
        :return: NoneType.
        :rtype: NoneType.
        """
        # base case
        if i >= len(nums):
            # need to append the current copy as the subset will keep changing
            self.res.append(subset.copy())
            return

        # decision to include nums[i]
        subset.append(nums[i])
        self.dfs(i + 1, subset, nums)

        # decision to NOT include nums[i]
        subset.pop()
        self.dfs(i + 1, subset, nums)
