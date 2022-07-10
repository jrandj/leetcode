from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the
        same color are adjacent, with the colors in the order red, white, and blue.

        We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

        You must solve this problem without using the library's sort function.

        :param nums : The input array.

        The time complexity is O(N) as we iterate through nums twice. Faster than 90.24% of solutions.

        The space complexity is O(N) for the hash map. Less memory than 62.66% of solutions.
        """
        colors = {}  # color : count

        for i, v in enumerate(nums):
            if colors.get(v) is None:
                colors[v] = 1
            else:
                colors[v] = colors.get(v) + 1

        for i, v in enumerate(nums):
            if colors.get(0) is not None and colors.get(0) != 0:
                nums[i] = 0
                colors[0] = colors.get(0) - 1
            elif colors.get(1) is not None and colors.get(1) != 0:
                nums[i] = 1
                colors[1] = colors.get(1) - 1
            elif colors.get(2) is not None and colors.get(2) != 0:
                nums[i] = 2
                colors[2] = colors.get(2) - 1
