from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k,
        and j != k, and nums[i] + nums[j] + nums[k] == 0.

        Notice that the solution set must not contain duplicate triplets.

        :param nums: The input list.
        :return List[List[int]: The output list of lists.

        The time complexity is O(LOG(N) + N^2) as we use sort and iterate through nums twice. Faster than 71.07% of
        solutions.

        The space complexity is O(N) as we sort. Less memory than 22.23% of solutions.

        """
        res = []
        nums.sort()

        for i, n in enumerate(nums):

            # skip over recurring values
            if i > 0 and n == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = n + nums[l] + nums[r]
                # too big
                if three_sum > 0:
                    r -= 1
                # too small
                elif three_sum < 0:
                    l += 1
                # found a 3Sum
                else:
                    res.append([n, nums[l], nums[r]])
                    # increment l skipping over duplicates
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res
