import heapq
from typing import List


class Solution:
    """
    Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted
    order, not the kth distinct element.

    Implement KthLargest class:

    KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
    int add(int val) Appends the integer val to the stream and returns the element representing the kth largest
    element in the stream.
    """

    def __init__(self, k: int, nums: List[int]):
        """
        Initialise the object.

        :param k: An integer representing the kth largest value.
        :type k: Int.
        :param nums: The input array.
        :type nums: List[int].

        The time complexity is O(N*LOG(N)). Faster than 36.25% of solutions.

        The space complexity is O(k). Less memory than 47.82 % of solutions.
        """
        self.minHeap = nums
        self.k = k
        # create a minHeap with the kth largest integers
        heapq.heapify(self.minHeap)
        # only keep the kth largest elements
        while len(self.minHeap) > k:
            # this removes the smallest element
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        """
        Append an integer to the stream and return the element representing the kth largest element in the stream.

        :param val: The value to add to the stream.
        :type val: Int.
        :return: The kth largest element.
        :rtype: Int.

        The time complexity is O(LOG(N)). Faster than 36.25% of solutions.

        The space complexity is O(k). Less memory than 47.82 % of solutions.
        """
        heapq.heappush(self.minHeap, val)
        # we only pop if we have less than k elements
        if len(self.minHeap) > self.k:
            # this removes the smallest element
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
