from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """Given an array of distinct integers candidates and a target integer target, return a list of all unique
        combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

        The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
        frequency of at least one of the chosen numbers is different.

        It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations
        for the given input.

        :param candidates: The list of candidates.
        :param target: The target number.
        :return List[List[int]: The list of combinations that sum to the target.

        The time complexity is O(K * 2^N') where K is the average length of each solution, and N' is the length of the
        new array. Faster than 26.10% of solutions.

        The space complexity is O(N) for the recursion stack and to hold the list. This depends on the length of
        the longest solution which is equal to target/min of candidates. Less memory than 27.13% of solutions.

        """
        self.res = []
        self.candidates = candidates
        self.target = target
        self.backtrack(0, [], 0)
        return self.res

    def backtrack(self, i, cur, total):
        # base cases
        if total == self.target:
            self.res.append(cur.copy())
            return
        if i >= len(self.candidates) or total > self.target:
            return

        cur.append(self.candidates[i])
        # this looks at the LHS (duplicates of current value)
        self.backtrack(i, cur, total + self.candidates[i])
        cur.pop()
        # this looks at the RHS (new elements)
        self.backtrack(i + 1, cur, total)
