from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """You are given an integer array height of length n. There are n vertical lines drawn such that the two
        endpoints of the ith line are (i, 0) and (i, height[i]). Find two lines that together with the x-axis form a
        container, such that the container contains the most water. Return the maximum amount of water a container
        can store. Notice that you may not slant the container.

        :param height: The height of the container.

        The time complexity is O(N) where N is the length of the input array. Faster than 92.32% of solutions.

        The space complexity is O(1) as no additional data structures are used. Less memory than 53.94% of solutions.

        """
        l, r = 0, len(height) - 1
        maxArea = -1

        while l < r:
            current_width = r - l
            current_height = min(height[l], height[r])
            maxArea = max(current_width * current_height, maxArea)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return maxArea
