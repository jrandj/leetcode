import heapq

from typing import List


class Solution:
    """
    Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any
    order.
    """

    def topKFrequent_heap(self, nums: List[int], k: int) -> List[int]:
        """
        Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in
        any order.

        :param nums: The input array.
        :type nums: List[Int].
        :param k: The number of most frequent elements.
        :type k: Int.
        :return: The k most frequent elements.
        :rtype: List[Int].

        The time complexity is O(N*LOG(K)) as we iterate over nums and on each iteration the heapq operations are
        O(LOG(K)). Faster than 93.7% of solutions.

        The space complexity is O(N) for the dictionary. Less memory than 70.57% of solutions.
        """
        freq = {}
        ans = []
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)

        for key, val in freq.items():
            if len(ans) < k:
                # push the element into the heap
                heapq.heappush(ans, [val, key])
            else:
                # push the element into the heap and return the smallest item from the heap
                heapq.heappushpop(ans, [val, key])

        # ans is left with the largest k values
        return [key for val, key in ans]

    def topKFrequent_bucket(self, nums: List[int], k: int) -> List[int]:
        """
        Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in
        any order.

        :param nums: The input array.
        :type nums: List[Int].
        :param k: The number of most frequent elements.
        :type k: Int.
        :return: The k most frequent elements.
        :rtype: List[Int].

        The time complexity is O(N) as we iterate through nums. Faster than 78.66% of solutions.

        The space complexity is O(N) for the list and dictionary. Less memory than 25.26% of solutions.
        """
        count = {}  # n, c
        freq = [[] for i in range(len(nums) + 1)]

        # find occurrences of each element
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            freq[c].append(n)

        res = []
        # the index of freq corresponds to count, so we iterate backwards through it
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
