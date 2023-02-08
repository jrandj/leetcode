import math
from typing import List


class Solution:
    """
    Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone
    and will come back in h hours.

    Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k
    bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more
    bananas during this hour.

    Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

    Return the minimum integer k such that she can eat all the bananas within h hours.
    """

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Return the minimum integer k such that she can eat all the bananas within h hours.

        :param piles: The array representing the piles of bananas.
        :type piles: List[Int].
        :param h: The hours we have to eat the bananas.
        :type h: Int.
        :return: The minimum value that all the bananas can be eaten in h hours.
        :rtype: Int.

        The time complexity is O(N*LOG(K)) where K is the largest element in piles. Faster than 55.67% of solutions.

        The space complexity is O(1). Less memory than 98.14%.
        """
        # try from 1 up to the max number in piles
        l, r = 1, max(piles)
        while l < r:
            k = l + (r - l) // 2
            # find how many hours with this k
            hours = 0
            for p in piles:
                # how many hours on this pile (rounding up)
                hours += math.ceil(p / k)

            if hours <= h:
                # we have an answer but there could be a smaller answer in the LHS
                r = k
            else:
                l = k + 1

        return l
