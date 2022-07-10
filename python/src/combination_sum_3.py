from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        """Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
            - Only numbers 1 through 9 are used.
            - Each number is used at most once.

        Return a list of all possible valid combinations. The list must not contain the same combination twice, and the
        combinations may be returned in any order.

        :param k: The number of combinations that sum to the target sum.
        :param n: The target sum.
        :return List[List[int]: The list of all possible combinations.

        The time complexity is O(k * 9^k) as the recursion depth is k and there are 9 digits to choose from. Faster
        than 82.38% of solutions.

        The space complexity is O(k) for the recursion stack and to hold the list. Less memory than 77.39% of
        solutions.
        """
        self.k = k
        self.n = n
        self.res = []

        self.backtrack(0, [], self.n)

        return self.res

    def backtrack(self, num, cur, target):
        # base cases
        if len(cur) == self.k:
            if target == 0:
                self.res.append(cur.copy())
            return

        for i in range(num + 1, 10):
            if i <= target:
                cur.append(i)
                self.backtrack(i, cur, target - i)
                cur.pop()
            else:
                return
