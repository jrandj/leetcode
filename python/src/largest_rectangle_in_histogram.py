from typing import List


class Solution:
    """
    Given an array of integers heights representing the histogram's bar height where the width of each bar is 1,
    return the area of the largest rectangle in the histogram.
    """

    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Calculate the largest rectangle area.

        :param heights: The list of histogram bar heights.
        :return int: The maximum rectangle height.

        The time complexity is O(N) where N is the length of heights. Faster than 44.78% of solutions.

        The space complexity is O(N) where N is the length of the stack. Less memory than 11.11% of solutions.
        """
        if not self.valid_input(heights):
            return 0

        max_area = 0
        stack = []  # pair: (index, height)

        for i, h in enumerate(heights):
            if h > int(1e4):
                return 0

            start = i
            # if current height is larger than top of the stack get rid of it
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            stack.append((start, h))

        # consider the remaining rectangles which run to the end
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        return max_area

    def valid_input(self, heights: List[int]) -> bool:
        """
        Validate the input that can be validated without iteration.

        :param heights: The list of histogram bar heights.
        :return bool: True if the input is valid, and false otherwise.
        """
        if len(heights) > int(1e5):
            return False
        return True
