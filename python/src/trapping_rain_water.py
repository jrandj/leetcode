from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how
        much water it can trap after raining.

        :param height: The list representing an elevation map.
        :return int: The amount of water that can be trapped.

        The time complexity is O(N) as we iterate through the input array once. Faster than 61.36% of solutions.

        The space complexity is O(1). Less memory than 33.69% of solutions.
        """
        l, r = 0, len(height) - 1
        left_max, right_max, res = height[l], height[r], 0

        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                res += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                res += right_max - height[r]

        return res
