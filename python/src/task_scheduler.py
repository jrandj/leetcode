import heapq
from collections import deque
from typing import List


class Solution:
    """
    Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a
    different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time,
    the CPU could complete either one task or just be idle.

    However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same
    letter in the array), that is that there must be at least n units of time between any two same tasks.

    Return the least number of units of times that the CPU will take to finish all the given tasks.
    """

    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Return the least number of units of times that the CPU will take to finish all the given tasks.

        :param tasks: The character array of tasks.
        :type tasks: List[Str].
        :param n: The idle time between two same tasks.
        :type n: Int.
        :return: The least number of units of times that the CPU will take to finish all the given tasks.
        :rtype: Int.

        The time complexity is O(N) as we iterate through the input array. Faster than 61.53% of solutions.

        The space complexity is O(N) for the heap. Less memory than 76.48% of solutions.
        """
        freq = {}
        for c in tasks:
            freq[c] = freq.get(c, 0) + 1
        # use negative values to create max heap
        maxHeap = [-cnt for cnt in freq.values()]
        heapq.heapify(maxHeap)

        # process most frequent first
        q = deque()  # pairs of [cnt, idleTime]
        time = 0
        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
