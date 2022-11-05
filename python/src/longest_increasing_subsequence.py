from typing import List


class Solution:
    """
    Given an integer array nums, return the length of the longest strictly increasing subsequence.

    A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the
    order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
    """

    def __init__(self):
        """
        Initialise the solution.
        """
        self.max_length = 0

    def lengthOfLIS_naive_memo(self, nums: List[int]) -> int:
        """
        Given an integer array nums, return the length of the longest strictly increasing subsequence.

        This is the brute force approach with memoization.

        :param nums: The input array.
        :type nums: List[Int].
        :return: The longest increasing subsequence.
        :rtype: Int.

        The time complexity is N^2 where N is the length of the nums. This solution results in time limit exceeded.

        The space complexity is O(N) for the memoization array. This solution results in time limit exceeded.
        """
        LIS = 0
        for i in range(len(nums)):
            LIS = max(LIS, self.dfs(i, nums, [0] * len(nums)))
        return LIS

    def dfs(self, i: int, nums: List[int], memo: List[int]) -> int:
        """
        A helper method to find the length of the longest increasing subsequence.

        :param i: The current index.
        :type i: Int.
        :param nums: The input array.
        :type nums: List[Int].
        :param memo: The memoization array.
        :type memo: List[Int].
        :return: The LIS at this index.
        :rtype: Int.
        """
        # base case
        if i == len(nums):
            return 0
        # use the cache
        if memo[i] > 0:
            return memo[i]
        LIS = 0
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                LIS = max(LIS, self.dfs(j, nums, memo))

        memo[i] = LIS + 1
        return LIS + 1

    def lengthOfLIS_naive(self, nums: List[int]) -> int:
        """
        Given an integer array nums, return the length of the longest strictly increasing subsequence.

        This is the brute force approach.

        :param nums: The input array.
        :type nums: List[Int].
        :return: The longest increasing subsequence.
        :rtype: Int.

        The time complexity is 2^N where N is the length of the nums. This solution results in time limit exceeded.

        The space complexity is O(N) for the current_list. This solution results in time limit exceeded.
        """
        # consider the substring beginning at each index
        for i in range(len(nums)):
            self.dfs_naive(nums, [nums[i]], i)
        return self.max_length

    def dfs_naive(self, nums: List[int], current_list: List[int], i: int):
        """
        A helper method to find the length of the longest increasing subsequence.

        :param nums: The input array.
        :type nums: List[Int].
        :param current_list: The current list.
        :type current_list: List[Int].
        :param i: The index that the current list starts from.
        :type i: Int.
        :return: NoneType.
        :rtype: NoneType.
        """
        self.max_length = max(len(current_list), self.max_length)
        if i == len(nums):
            return
        # consider the rest of the string starting at i
        for j in range(i + 1, len(nums)):
            # at every index we can add or not add the value
            if nums[i] < nums[j]:
                current_list.append(nums[j])
                self.dfs_naive(nums, current_list, j)
                current_list.remove(nums[j])

    def lengthOfLIS_iterative(self, nums: List[int]) -> int:
        """
        Given an integer array nums, return the length of the longest strictly increasing subsequence.

        :param nums: The input array.
        :type nums: List[Int].
        :return: The longest increasing subsequence.
        :rtype: Int.

        The time complexity is O(N^2) as we use a nested for loop. Faster than 53.67% of solutions.

        The space complexity is O(N) to hold the LIS array. Less memory than 45.00% of solutions.
        """
        LIS = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        return max(LIS)
