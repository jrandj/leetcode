from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """Given a collection of candidate numbers (candidates) and a target number (target), find all unique
        combinations in candidates where the candidate numbers sum to target.

        Each number in candidates may only be used once in the combination.

        Note: The solution set must not contain duplicate combinations.

        :param candidates: The list of candidates.
        :param target: The target number.
        :return List[List[int]: The list of combinations that sum to the target.

        The time complexity is O(K * 2^N) where K is the average length of each solution and N is the length of the
        input list. Faster than 20.65% of solutions.

        The space complexity is O(N) for the recursion stack and to hold the list. This depends on the length of
        the longest solution which is equal to target/min of candidates. Less memory than 57.10% of solutions.
        """
        self.res = []
        self.candidates = candidates
        self.target = target

        # sort the array so that we can skip duplicates
        self.candidates.sort()
        self.backtrack(0, [], 0)

        return self.res

    def backtrack(self, pos, cur, total):
        # base cases
        if total == self.target:
            self.res.append(cur.copy())
            return
        if total >= self.target:
            return

        prev_value = -1
        for i in range(pos, len(self.candidates)):
            # skip duplicates
            if self.candidates[i] == prev_value:
                continue
            cur.append(self.candidates[i])
            self.backtrack(i + 1, cur, total + self.candidates[i])
            cur.pop()
            prev_value = self.candidates[i]
