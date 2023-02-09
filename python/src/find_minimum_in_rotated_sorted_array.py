from typing import List


class Solution:
    """
    Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array
    nums = [0,1,2,4,5,6,7] might become:

    [4,5,6,7,0,1,2] if it was rotated 4 times.
    [0,1,2,4,5,6,7] if it was rotated 7 times.

    Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1],
    a[2], ..., a[n-2]].

    Given the sorted rotated array nums of unique elements, return the minimum element of this array.

    You must write an algorithm that runs in O(log n) time.
    """

    def findMin(self, nums: List[int]) -> int:
        """
        Given the sorted rotated array nums of unique elements, return the minimum element of this array.

        :param nums: The array of unique elements.
        :type nums: List[Int].
        :return: The minimum value in nums.
        :rtype: Int.

        The time complexity is O(LOG(N)). Faster than 53.11% of solutions.

        The space complexity is O(1). Less memory th an 17.38% of solutions.
        """
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            # search RHS
            if nums[m] > nums[r]:
                l = m + 1
            # search LHS
            else:
                r = m
        return nums[l]
