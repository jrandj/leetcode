from typing import List
import heapq


class Solution:
    """
    Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return
    the k closest points to the origin (0, 0).

    The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

    You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
    """

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Return the k closest points to the origin (0, 0).

        :param points: The input points.
        :type points: List[List[Int]].
        :param k: The k closest points.
        :type k: Int.
        :return: The k closest poins to the origin (0, 0).
        :rtype: List[List[Int]].

        The time complexity is O(N + N*(LOG(N)) to create the minHeap and pop from it up to N times. Faster than
        71.19% of solutions.

        The space complexity is O(N) to store the minHeap. Less memory than 24.88% of solutions.
        """
        minHeap, res = [], []
        for p in points:
            # we don't need to calculate the sqrt
            minHeap.append([p[0] * p[0] + p[1] * p[1], p[0], p[1]])
        heapq.heapify(minHeap)

        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
        return res
