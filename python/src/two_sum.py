from typing import List


class Solution:
    def two_sum_a(self, nums: List[int], target: int) -> List[int]:
        """Given an array of integers nums and an integer target, return indices of the two numbers such that they add
        up to target. You may assume that each input would have exactly one solution, and you may not use the same
        element twice. You can return the answer in any order.

        :param nums: The input array.
        :param target: The target number:
        :return List[int]: A list of indices.

        The time complexity is O(N^2) as we use 2 nested for loops. Faster than 22.50% of solutions.

        The space complexity is constant. Less memory than 76.44% of solutions.

        """
        for i, iVal in enumerate(nums):
            # we only need to look for the elements after the current element
            for j, jVal in enumerate(nums[1 + i:]):
                if iVal + jVal == target:
                    # we cut the array from 1 + i, so we need to add that back for the 2nd index
                    return [i, i + j + 1]

    def two_sum_b(self, nums: List[int], target: int) -> List[int]:
        """Given an array of integers nums and an integer target, return indices of the two numbers such that they add
        up to target. You may assume that each input would have exactly one solution, and you may not use the same
        element twice. You can return the answer in any order.

        :param nums: The input array.
        :param target: The target number:
        :return List[int]: A list of indices.

        The time complexity is O(N) as we iterate over the array once. Faster than 88.91% of solutions.

        The space complexity is O(N) for the hash map. Less memory than 24.32% of solutions.

        """
        existing_values = {}  # hash map containing val: index
        for i, iVal in enumerate(nums):
            diff = target - iVal
            if diff in existing_values:
                return [existing_values[diff], i]
            existing_values[iVal] = i
        # guaranteed to have a solution so don't need a return here
