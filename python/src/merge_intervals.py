from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and
        return an array of the non-overlapping intervals that cover all the intervals in the input.

        :param intervals: The input intervals.
        :return List[List[int]: The list of overlapping intervals.

        The time complexity is O(N * LOG(N)) due to sorting, where N is the length of candidates. Faster than 68.33%
        of solutions.

        The space complexity is O(N) to hold the output list. Less memory than 24.84% of solutions.

        """
        # sort the input array by the lowest interval
        intervals.sort(key=lambda i: i[0])
        res = [intervals[0]]

        for start, end in intervals[1:]:
            last_end = res[-1][1]
            if start <= last_end:
                res[-1][1] = max(last_end, end)
            else:
                res.append([start, end])

        return res
