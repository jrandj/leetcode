import heapq
from typing import List


class Solution:
    """
    Given an integer array nums and an integer k, return the kth largest element in the array.

    Note that it is the kth largest element in the sorted order, not the kth distinct element.

    Can you solve it without sorting?
    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Given an integer array nums and an integer k, return the kth largest element in the array.

        :param nums: The input array.
        :type nums: List[Int].
        :param k: The kth largest element.
        :type k: In.
        :return: The kth largest element in nums.
        :rtype: Int.

        The time complexity is O(N + N*LOG(N)) to heapify a list and pop up to N times from it. Faster than 51.38% of
        solutions.

        The space complexity is O(N) to store the heap. Less memory than 26.15% of solutions.
        """
        heap = [x * -1 for x in nums]
        heapq.heapify(heap)
        while k > 0:
            res = heapq.heappop(heap) * -1
            k -= 1
        return res
