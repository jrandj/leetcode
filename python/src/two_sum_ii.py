from typing import List


class Solution:
    """
    Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such
    that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where
    1 <= index1 < index2 <= numbers.length.

    Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of
    length 2.

    The tests are generated such that there is exactly one solution. You may not use the same element twice.

    Your solution must use only constant extra space.
    """

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of
        length 2.

        :param numbers: The array of sorted input numbers.
        :type numbers: List[int].
        :param target: The target number for the sum.
        :type target: Int.
        :return: The indices (+1 for each) of the two numbers that sum to the target.
        :rtype: List[int].

        The time complexity is O(N) as we iterate through the array only once. Faster than 22.36% of solutions.

        The space complexity is O(1) as we don't use any additional data structures. Less memory than 89.02% of
        solutions.
        """
        l, r = 0, len(numbers) - 1

        while l < r:
            cur = numbers[l] + numbers[r]
            if cur > target:
                r -= 1
            elif cur < target:
                l += 1
            else:
                return [l + 1, r + 1]
