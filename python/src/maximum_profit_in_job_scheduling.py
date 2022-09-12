from functools import lru_cache
from typing import List


class Solution:
    """
    We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of
    profit[i].

    You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no
    two jobs in the subset with overlapping time range.

    If you choose a job that ends at time X you will be able to start another job that starts at time X.
    """

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """
        Return the maximum profit you can take such that there are no two jobs in the subset with overlapping time
        range.

        :param startTime: The starting times of the jobs.
        :type startTime: List[int].
        :param endTime: The ending times of the jobs.
        :type endTime: List[int].
        :param profit: The profit for each of the jobs.
        :type profit: List[int].
        :return: The maximum profit without any overlapping jobs.
        :rtype: Int.

        The time complexity is O(N LOG(N)) as we do N binary searches. Faster than 13.71% of solutions.

        The space complexity is O(N) for the recursive stack. Less memory than 5.07% of solutions.
        """
        # sort by start time so we can use binary search
        self.jobs = sorted(zip(startTime, endTime, profit))
        self.startTimes = [job[0] for job in self.jobs]
        return self.dp(0)

    @lru_cache(None)
    def dp(self, i: int):
        """
        A helper method for job scheduling. Use lru_cache to remember common input/outputs for optimisation.

        :param i: The starting time for the job.
        :type i: Int.
        :return: The maximum profit.
        :rtype: Int.
        """
        if i >= len(self.startTimes):
            return 0

        # find the index of the next job that starts after the current end time
        new_i = self.bisect_left(self.startTimes, self.jobs[i][1])
        # we can either take the current job and get its profit, or skip it and move to the next one
        return max(self.dp(i + 1), self.jobs[i][2] + self.dp(new_i))

    def bisect_left(self, a: List[int], x: int):
        """
        A simple bisect_left implementation, ideally you can just use bisect.bisect_left.

        The return value i is such that all e in a[:i] have e < x, and all e in a[i:] have e >= x.  So if x already
        appears in the list, a.insert(i, x) will insert just before the leftmost x already there.

        :param a: The list for comparison.
        :type a: List[int].
        :param x: The value to find the index for.
        :type x: Int.
        :return: The value such that all e in a[:i] have e < x, and all e in a[i:] have e >= x
        :rtype: Int.
        """
        low, high = 0, len(a)
        while low < high:
            # equivalent to mid = (low + high) // 2
            mid = low + (high - low) // 2
            if a[mid] < x:
                low = mid + 1
            else:
                high = mid
        return low
