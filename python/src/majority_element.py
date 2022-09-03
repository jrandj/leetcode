from typing import List


class Solution:
    def majorityElement_a(self, nums: List[int]) -> int:
        """
        Given an array nums of size n, return the majority element.

        The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority
        element always exists in the array.

        :param nums: The input array.
        :type nums: List[int].
        :return: The majority element.
        :rtype: Int.

        The time complexity is O(N) as we iterate through the input array once. Faster than 28.65% of solutions.

        The space complexity is O(N) as we use a Hash Map containing all elements. Less memory than 34.94% of solutions.
        """
        values = {}
        candidate_result, max_count = 0, 0

        for n in nums:
            values[n] = 1 + values.get(n, 0)
            if values[n] > max_count:
                candidate_result = n
                max_count = values[n]

        return candidate_result

    def majorityElement_b(self, nums: List[int]) -> int:
        """
        Given an array nums of size n, return the majority element.

        The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority
        element always exists in the array.

        :param nums: The input array.
        :type nums: List[int].
        :return: The majority element.
        :rtype: Int.

        The time complexity is O(N) as we iterate through the input array once. Faster than 69.51% of solutions.

        The space complexity is O(1) as we only use constants. Less memory than 34.94% of solutions.
        """
        candidate_result, count = 0, 0

        for n in nums:
            if count == 0:
                candidate_result = n

            count += (1 if n == candidate_result else -1)

        return candidate_result
