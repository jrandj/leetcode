import sys
from typing import List


class Solution:
    """
    You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

    Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

    You may assume that you have an infinite number of each kind of coin.
    """

    def __init__(self):
        """
        Initialise the solution.
        """
        self.cache = {}
        self.result = sys.maxsize

    def coinChange_recursive(self, coins: List[int], amount: int) -> int:
        """
        Return the fewest number of coins that you need to make up that amount.

        :param coins: The coins available to make up the total.
        :type coins: List[Int].
        :param amount: The amount that needs to be made up.
        :type amount: Int.
        :return: The minimum number of coins that make up the amount, with -1 indicating no possible result.
        :rtype: Int.

        The time complexity of the naive approach is O(K^M), where M is the amount and K is the number of coins. By
        caching the result we reduce the complexity to O(K). Faster than 18.75% of solutions.

        The space complexity is O(K) for the recursive calls and the cache. Less memory than 19.51% of solutions.
        """
        res = self.dfs(coins, amount)
        return res

    def dfs(self, coins: List[int], target: int):
        """
        A helper method for coinChange_recursive.

        :param coins: The coins available to make up the total.
        :type coins: List[Int].
        :param target: The amount that needs to be made up.
        :type target: Int.
        :return: The minimum number of coins that make up the target, with -1 indicating no possible result.
        :rtype: Int.
        """
        # base case
        if target == 0:
            return 0
        min_count = sys.maxsize
        for i in range(len(coins)):
            # check if we can use this coin to reach our target
            if coins[i] <= target:
                # check the cache! avoid unnecessary recursive calls
                current_count = self.cache.get(target - coins[i], None)
                if not current_count:
                    # pick this coin and subtract it from the remaining amount
                    current_count = self.dfs(coins, target - coins[i])
                    self.cache[target - coins[i]] = current_count

                # keep the count if it is an improvement
                if current_count != -1 and current_count + 1 < min_count:
                    min_count = current_count + 1

        # handle the scenario where no combination of coins can reach the amount
        if min_count == sys.maxsize:
            return -1

        return min_count

    def coinChange_iterative(self, coins: List[int], amount: int) -> int:
        """
        Return the fewest number of coins that you need to make up that amount.

        :param coins: The coins available to make up the total.
        :type coins: List[Int].
        :param amount: The amount that needs to be made up.
        :type amount: Int.
        :return: The minimum number of coins that make up the amount, with -1 indicating no possible result.
        :rtype: Int.

        The time complexity is O(M*K), where M is the amount and K is the number of coins. Faster than 11.70% of
        solutions.

        The space complexity is O(M) for the DP array. Less memory than 60.44% of solutions.
        """
        dp = [sys.maxsize] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                target = a - c
                if target >= 0:
                    # find possible solutions
                    dp[a] = min(dp[a], 1 + dp[a - c])

        return dp[amount] if dp[amount] != sys.maxsize else -1
