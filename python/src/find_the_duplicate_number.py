from typing import List


class Solution:
    """
    Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

    There is only one repeated number in nums, return this repeated number.

    You must solve the problem without modifying the array nums and uses only constant extra space.
    """

    def findDuplicate(self, nums: List[int]) -> int:
        """
        Return the duplicate number in nums.

        :param nums: The list of integers.
        :type nums: List[Int].
        :return: The repeated number.
        :rtype: Int.

        The time complexity is O(N) to iterate through the list. Faster than 52.51% of solutions.

        The space complexity is O(1). Less memory than 74.86% of solutions.
        """
        slow, fast = 0, 0

        slow = nums[slow]
        fast = nums[nums[fast]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow2
