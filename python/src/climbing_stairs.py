class Solution:
    """
    You are climbing a staircase. It takes n steps to reach the top.

    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
    """

    def climbStairs(self, n: int) -> int:
        """
        Find the number of distinct ways you can climb to the top.

        :param n: The number of steps to the type.
        :type n: Int.
        :return: The number of distinct ways you can climb to the top.
        :rtype: Int.

        The time complexity is O(N) as we iterate up to n. Faster than 28.31% of solutions.

        The space complexity is O(N) for the array. Less memory than 96.12% of solutions.
        """
        if n < 1 or n > 45:
            return 0

        res = [1, 2]
        for i in range(2, n):
            res.append(res[i - 1] + res[i - 2])

        return res[n - 1]
