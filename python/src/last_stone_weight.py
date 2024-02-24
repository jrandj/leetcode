import heapq
from typing import List


class Solution:
    """
    You are given an array of integers stones where stones[i] is the weight of the ith stone.

    We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together.
    Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

    If x == y, both stones are destroyed, and
    If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.

    At the end of the game, there is at most one stone left.

    Return the weight of the last remaining stone. If there are no stones left, return 0.
    """

    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        Return the weight of the last remaining stone. If there are no stones left, return 0.

        :param stones: The array representing the weight of stones.
        :type stones: List[Int].
        :return: The weight of the last remaining stone.
        :rtype: Int.

        The time complexity is O(N*LOG(N)) as we create a heap and then pop from it. Faster than 75.14% of solutions.

        The space complexity is O(N) as we create a heap of size N. Less memory than 96.39% of solutions.
        """
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)
            diff = -abs(first - second)
            heapq.heappush(stones, diff)

        return abs(stones[0])
