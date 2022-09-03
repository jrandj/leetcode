from typing import List


class Solution:
    """
    There is an integer array nums sorted in ascending order (with distinct values).

    Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
    such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
    For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

    Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums,
    or -1 if it is not in nums.

    You must write an algorithm with O(log n) runtime complexity.
    """

    def search(self, nums: List[int], target: int) -> int:
        """
        Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums,
        or -1 if it is not in nums.

        :param nums: An array sorted in ascended order and rotated around a pivot.
        :type nums: List[int]
        :param target: The value at the pivot index.
        :type target: Int.
        :return: The index of target.
        :rtype: Int.

        The time complexity is O(LOG(N)) as we use binary search. Faster than 5.45% of solutions.

        The space complexity is O(1) as we don't use any additional data structures. Less memory than 56.61% of
        solutions.
        """
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid

            # LHS is strictly increasing
            if nums[mid] >= nums[l]:
                # check if target is in LHS
                if nums[mid] >= target >= nums[l]:
                    r = mid - 1
                # if not present in LHS must be in RHS
                else:
                    l = mid + 1
            # if LHS is not strictly increasing RHS must be
            else:
                # check if target is in RHS
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                # if not present in RHS must be in LHS
                else:
                    r = mid - 1

        return -1
