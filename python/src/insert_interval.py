from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent
        the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also
        given an interval newInterval = [start, end] that represents the start and end of another interval.

        Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and
        intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

        Return intervals after the insertion.

        :param intervals: A list of intervals.
        :param newInterval: A new interval for insertion.
        :return List[List[int]: A list of a list of intervals.

        The time complexity is O(N) as we use iterate through intervals once. Faster than 97.70% of solutions.

        The space complexity is O(N) as we create a new list of N elements. Less memory than 24.91% of solutions.

        """
        final_list = []

        for i, n in enumerate(intervals):
            l, r = n[0], n[1]
            new_l, new_r = newInterval[0], newInterval[1]
            # the interval goes before all other intervals
            if new_r < l:
                final_list.append(newInterval)
                return final_list + intervals[i:]
            # the interval goes before current interval
            elif new_l > r:
                final_list.append(intervals[i])
            # the intervals are overlapping
            else:
                newInterval = [min(l, new_l), max(r, new_r)]

        final_list.append(newInterval)
        return final_list
