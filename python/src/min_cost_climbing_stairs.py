from typing import List


class Solution:
    """
    You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost,
    you can either climb one or two steps.

    You can either start from the step with index 0, or the step with index 1.

    Return the minimum cost to reach the top of the floor.
    """

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Return the minimum cost to reach the top of the floor.

        :param cost: The list of costs to climb the ith step.
        :type cost: Int.
        :return: The cost of climbing to the top.
        :rtype: Int.

        The time complexity is O(N) as we iterate over the length of cost. Faster than 10.62% of solutions.

        The space complexity is O(N) for the dp list. Less memory than 42.18% of solutions.
        """
        if not cost:
            return 0

        # memorise the min cost at the ith step
        dp = [cost[0]]
        if len(cost) >= 2:
            dp.append(cost[1])

        # go up to len(cost) because we are really at the step after cost[-1]
        for i in range(2, len(cost)):
            dp.append(cost[i] + min(dp[i - 1], dp[i - 2]))
        return min(dp[-1], dp[-2])
