import collections
from typing import List


class Solution:
    """
    Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), return the number of
    islands.

    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may
    assume all four edges of the grid are all surrounded by water.
    """

    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), return the number of
        islands.

        An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may
        assume all four edges of the grid are all surrounded by water.

        :param grid: The grid representing a map of land and water.
        :type grid: List[List[Str]]
        :return: The number of islands.
        :rtype: Int.

        The time complexity is O(N*M) to visit each cell. Faster than 19.78% of solutions.

        The space complexity is O(N*M) to store the queue. Less memory than 36.36% of solutions.
        """
        if not grid or not grid[0]:
            return None

        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        visited = set()

        def search(px: int, py: int, mode: str) -> None:
            q = collections.deque()
            visited.add((px, py))
            q.append((px, py))

            while q:
                if mode == "bfs":
                    # pop oldest (append adds at the right end)
                    ax, ay = q.popleft()
                elif mode == "dfs":
                    # pop most recent (append adds at the right end)
                    ax, ay = q.pop()
                else:
                    raise ValueError("Supported modes are bfs and dfs")
                # left right up down
                directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
                for dx, dy in directions:
                    r, c = ax + dx, ay + dy
                    if r in range(rows) and c in range(cols) and (r, c) not in visited and grid[r][c] == "1":
                        visited.add((r, c))
                        q.append((r, c))

        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == "1" and (x, y) not in visited:
                    search(x, y, "bfs")
                    islands += 1
        return islands
