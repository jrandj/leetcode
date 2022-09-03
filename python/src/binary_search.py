from typing import List


class Solution:
    """
    Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to
    search target in nums. If target exists, then return its index. Otherwise, return -1.

    You must write an algorithm with O(log n) runtime complexity.
    """

    def search(self, nums: List[int], target: int) -> int:
        """
        Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to
        search target in nums. If target exists, then return its index. Otherwise, return -1.

        :param nums: The array of integer nums.
        :type nums: List[int].
        :param target: The integer target.
        :type target: Int.
        :return: The index of the target if it exists in nums, and -1 if it is not found.
        :rtype: Int.

        The time complexity is O(N LOG(N)) as we halve the search space each iteration. Faster than 14.93% of solutions.

        The space complexity is O(1) as we don't use any additional data structures. Less memory than 72.77% of
        solutions.
        """
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2
            if nums[m] > target:
                # exclude m:r from search space
                r = m - 1
            elif nums[m] < target:
                # exclude l:m from search space
                l = m + 1
            else:
                return m
        return -1
