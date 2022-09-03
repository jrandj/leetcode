from typing import List


class Solution:
    def containsDuplicate_a(self, nums: List[int]) -> bool:
        """
        Given an integer array nums, return true if any value appears at least twice in the array, and return false
        if every element is distinct.

        :param nums: The input array.
        :type nums: Int.
        :return: True if any value appears at least twice and false otherwise.
        :rtype: Bool.

        The time complexity is O(N) as we iterate through the input array once. Faster than 17.13% of solutions.

        The space complexity is O(N) as we use a Hash Map containing all elements. Less memory than 72.28% of solutions.
        """
        unique_values = {}  # value: count

        for n in nums:
            current_value = unique_values.get(n)

            if current_value is None:
                unique_values[n] = 1
            else:
                return True

        return False

    def containsDuplicate_b(self, nums: List[int]) -> bool:
        """
        Given an integer array nums, return true if any value appears at least twice in the array, and return false
        if every element is distinct.

        :param nums: The input array.
        :type nums: List[int].
        :return: True if any value appears at least twice and false otherwise.
        :rtype: Bool.

        The time complexity is O(N LOG(N)) as we sort the array. Faster than 52.77% of solutions.

        The space complexity is O(1) as we only use constants. Less memory than 29.99% of solutions.
        """
        l, r = 0, 1
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[l] != nums[r]:
                l += 1
                r += 1
            else:
                return True

        return False
