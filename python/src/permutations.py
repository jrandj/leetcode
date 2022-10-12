from typing import List


class Solution:
    """
    Given an array nums of distinct integers, return all the possible permutations.

    You can return the answer in any order.
    """

    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Given an array nums of distinct integers, return all the possible permutations.

        :param nums: The input array of distinct integers.
        :type nums: List[int].
        :return: All possible permutations.
        :rtype: List[List[int]].

        The time complexity is O(N*N!) as there are N! branches and for each iteration we need to append to an array
        which is O(N). Faster than 56.88% of solutions.

        The space complexity is O(N*N!) as we have N! answers and each one is of length N. Less memory than 58.97% of
        solutions.
        """
        if not nums:
            return [[]]

        res = []
        if len(nums) == 1:
            return [nums.copy()]

        for i in range(len(nums)):
            # pop off first element and recurse
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                # add n back
                perm.append(n)
                res.append(perm)
            nums.append(n)

        return res
