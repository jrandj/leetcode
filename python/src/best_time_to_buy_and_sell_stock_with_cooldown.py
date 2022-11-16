from typing import List


class Solution:
    """
    You are given an array prices where prices[i] is the price of a given stock on the ith day.

    Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell
    one share of the stock multiple times) with the following restrictions:

    After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).

    Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy
    again).
    """

    def __init__(self):
        """
        Initialise the solution.
        """
        self.dp = None
        self.prices = None

    def maxProfit_recursion(self, prices: List[int]) -> int:
        """
        Find the maximum profit you can achieve.

        :param prices: The stock prices.
        :type prices: List[Int].
        :return: The maximum profit.
        :rtype: Int.

        The time complexity is O(N) as we use memoization. Faster than 13.63% of solutions.

        The space complexity is O(N) for the recursion stack and the memoization dict. Less memory than 24.55% of
        solutions.
        """
        self.dp = {}  # (i, canBuy) -> val
        self.prices = prices
        return self.dfs(0, True)

    def dfs(self, i: int, canBuy: bool) -> int:
        """
        A helper method for maxProfit.

        :param i: The current index.
        :type i: Int.
        :param canBuy: Whether we can buy or sell.
        :type canBuy: Bool.
        :return: The maximum profit at the current index.
        :rtype: Int.
        """
        # base case
        if i >= len(self.prices):
            return 0
        # check cache
        elif (i, canBuy) in self.dp:
            return self.dp[(i, canBuy)]

        # we can not buy or sell at any time
        cooldown = self.dfs(i + 1, canBuy)
        # we can either buy or sell, but if we sell we skip an extra day
        if canBuy:
            buy = self.dfs(i + 1, not canBuy) - self.prices[i]
            self.dp[(i, canBuy)] = max(buy, cooldown)
        else:
            sell = self.dfs(i + 2, not canBuy) + self.prices[i]
            self.dp[(i, canBuy)] = max(sell, cooldown)
        return self.dp[(i, canBuy)]

    def maxProfit_dfs(self, prices: List[int]) -> int:
        """
        Find the maximum profit you can achieve.

        :param prices: The stock prices.
        :type prices: List[Int].
        :return: The maximum profit.
        :rtype: Int.

        The time complexity is O(N) as we iterate through the array. Faster than 47.02% of solutions.

        The space complexity is O(1) as we only use constants. Less memory than 81.81% of solutions.
        """
        # dp[i][sell] = max(dp[i-1][sell], dp[i-1][buy]+price)
        # dp[i][buy] = max(dp[i-1][buy], dp[i-1][cooldown]-price)
        # dp[i][cooldown] = max(dp[i-1][cooldown], dp[i-1][sell])

        dp_prev = [0, -1 * float("inf"), 0]  # sell, buy, cooldown
        dp_curr = [0, 0, 0]

        for price in prices:
            dp_curr[0] = max(dp_prev[0], dp_prev[1] + price)
            dp_curr[1] = max(dp_prev[1], dp_prev[2] - price)
            dp_curr[2] = max(dp_prev[2], dp_prev[0])
            dp_prev = dp_curr
            dp_curr = [0, 0, 0]
        return dp_prev[0]
