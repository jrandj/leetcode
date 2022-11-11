from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to
        maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to
        sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve
        any profit, return 0.

        :param prices: The input array.
        :type prices: List[int].
        :return: The maximum profit that can be achieved.
        :rtype: Int.

        The time complexity is O(N) as we iterate through the input array once. Faster than 89.82% of solutions.

        The space complexity is constant. Less memory than 7.11% of solutions.
        """
        # this solution requires that we can "see the future" (1 + ith element)
        max_profit, left_pointer, right_pointer = 0, 0, 1

        while right_pointer < len(prices):
            # check if profitable
            if prices[left_pointer] < prices[right_pointer]:
                profit = prices[right_pointer] - prices[left_pointer]
                if profit > max_profit:
                    max_profit = profit
            else:
                # keep looking
                left_pointer = right_pointer

            right_pointer += 1

        return max_profit
