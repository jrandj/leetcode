from typing import List


class Solution:
    """
    There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The
    robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or
    right at any point in time.

    Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the
    bottom-right corner.

    The test cases are generated so that the answer will be less than or equal to 2 * 109.
    """

    def __init__(self):
        self.paths = None

    def uniquePaths_recursive(self, m: int, n: int) -> int:
        """
        Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the
        bottom-right corner.

        This is the naive approach.

        :param m: The number of rows.
        :type m: Int.
        :param n: The number of columns.
        :type n: Int.
        :return: The number of unique paths.
        :rtype: Int.

        The time complexity is O(2^(M*N)). Results in time limit exceeded.

        The space complexity is O(2^(M*N)). Results in time limit exceeded.
        """
        self.paths = []
        self.dfs(m, n, 0, 0, [])
        return len(self.paths)

    def dfs(self, m: int, n: int, i: int, j: int, path: List[int]):
        """
        A helper method to perform a Depth-First Search.

        :param m: The number of rows.
        :type m: Int.
        :param n: The number of columns.
        :type n: Int.
        :param i: The current row.
        :type i: Int.
        :param j: The current column.
        :type j: Int.
        :param path: The current path.
        :type path: List[Int].
        :return: NoneType.
        :rtype: NoneType.
        """
        # base case
        if i == m - 1 and j == n - 1:
            self.paths.append(path)
            return

        # check bounds
        if i >= m or j >= n:
            return

        self.dfs(m, n, i + 1, j, path) or self.dfs(m, n, i, j + 1, path)

    def uniquePaths_iterative(self, m: int, n: int) -> int:
        """
        Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the
        bottom-right corner.

        This is the naive approach.

        :param m: The number of rows.
        :type m: Int.
        :param n: The number of columns.
        :type n: Int.
        :return: The number of unique paths.
        :rtype: Int.

        The time complexity is O(M*N). Faster than 61.09% of solutions.

        The space complexity is O(M*N). Less memory than 73.94% of solutions.
        """
        dp = [[0] * n for i in range(m)]
        for r in range(m):
            for c in range(n):
                if r == 0 or c == 0:
                    dp[r][c] = 1
                else:
                    dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        return dp[m - 1][n - 1]
