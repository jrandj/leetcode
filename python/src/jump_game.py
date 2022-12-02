from typing import List


class Solution:
    """
    You are given an integer array nums. You are initially positioned at the array's first index, and each element in
    the array represents your maximum jump length at that position.

    Return true if you can reach the last index, or false otherwise.
    """

    def __init__(self):
        """
        Initialise the solution.
        """
        self.memo = None
        self.res = None

    def canJump_naive(self, nums: List[int]) -> bool:
        """
        Return true if you can reach the last index, or false otherwise.

        :param nums: The integer array.
        :type nums: List[Int].
        :return: True if you can jump to the end of the array, and False otherwise.
        :rtype: Bool.

        The time complexity is O(N^N). Results in Time Limit Exceeded.

        The space complexity is O(N) for the recursive stack. Results in Time Limit Exceeded.
        """
        self.res = False
        self.dfs_naive(0, nums)
        return self.res

    def canJump_memo(self, nums: List[int]) -> bool:
        """
        Return true if you can reach the last index, or false otherwise.

        :param nums: The integer array.
        :type nums: List[Int].
        :return: True if you can jump to the end of the array, and False otherwise.
        :rtype: Bool.

        The time complexity is O(2^N). Results in Time Limit Exceeded.

        The space complexity is O(N) for the recursive stack and memoization dict. Results in Time Limit Exceeded.
        """
        self.memo = {}
        self.dfs_memo(0, nums)
        return self.dfs_memo(0, nums)

    def canJump_dfs(self, nums: List[int]) -> bool:
        """
        Return true if you can reach the last index, or false otherwise.

        :param nums: The integer array.
        :type nums: List[Int].
        :return: True if you can jump to the end of the array, and False otherwise.
        :rtype: Bool.

        The time complexity is O(N). Faster than 97.00% of solutions.

        The space complexity is O(1) as we don't use any additional data structures. Less memory than 49.40% of
        solutions.
        """
        goal = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            # if we can get to the end from here then this is the new goal
            if i + nums[i] >= goal:
                goal = i

        # if goal is 0 we can get to the end from the start!
        return True if goal == 0 else False

    def dfs_memo(self, i: int, nums: List[int]):
        """
        A helper method to perform a Depth-First Search (DFS).

        :param i: The current index.
        :type i: Int.
        :param nums: The integer array.
        :type nums: List[Int].
        :return: NoneType.
        :rtype: NoneType.
        """
        if i >= len(nums):
            return False
        elif i == len(nums) - 1:
            return True
        elif i in self.memo:
            return self.memo[i]
        else:
            self.memo[i] = False
            jumps = nums[i]
            while jumps > 0:
                if self.dfs_memo(i + jumps, nums):
                    self.memo[i] = True
                    return self.memo[i]
                jumps -= 1
            return self.memo[i]

    def dfs_naive(self, i: int, nums: List[int]):
        """
        A helper method to perform a Depth-First Search (DFS).

        :param i: The current index.
        :type i: Int.
        :param nums: The integer array.
        :type nums: List[Int].
        :return: NoneType.
        :rtype: NoneType.
        """
        if i >= len(nums) - 1:
            self.res = True
            return
        jumps = nums[i]
        while jumps > 0:
            self.dfs_naive(i + jumps, nums)
            jumps -= 1
