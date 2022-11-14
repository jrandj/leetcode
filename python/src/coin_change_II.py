from typing import List


class Solution:
    """
    You are given an integer array coins representing coins of different denominations and an integer amount
    representing a total amount of money.

    Return the number of combinations that make up that amount. If that amount of money cannot be made up by any
    combination of the coins, return 0.

    You may assume that you have an infinite number of each kind of coin.

    The answer is guaranteed to fit into a signed 32-bit integer.
    """

    def __init__(self):
        """
        Initialise the solution.
        """
        self.count = 0
        self.memo = {}

    def change(self, amount: int, coins: List[int]) -> int:
        """
        Return the number of combinations that make up the amount.

        :param amount: The target amount.
        :type amount: Int.
        :param coins: The coins available for selection.
        :type coins: List[Int].
        :return: The number of combinations that make up the amount.
        :rtype: Int.

        The time complexity is O(M*N). Faster than 5.02% of solutions.

        The space complexity is O(M*N) for the cache and recursion stack. Less memory than 22.88% of solutions.
        """
        if not coins:
            return 0
        return self.dfs(0, amount, coins)

    def dfs(self, index: int, remainder: int, coins: int) -> int:
        """
        A helper method to perform a Depth-First Search (DFS).

        :param index: The current index.
        :type index: Int.
        :param remainder: The remaining amount.
        :type remainder: Int.
        :param coins: The coins available for selection.
        :type coins: List[Int].
        :return: The number of combinations that make up the amount at the current index.
        :rtype: Int.
        """
        # base cases
        if remainder == 0:
            return 1
        if (index, remainder) in self.memo:
            return self.memo[(index, remainder)]

        res = 0
        for i in range(index, len(coins)):
            if remainder - coins[i] >= 0:
                res += self.dfs(i, remainder - coins[i], coins)
        self.memo[(index, remainder)] = res
        return self.memo[(index, remainder)]
