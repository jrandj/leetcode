package leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

/**
 * Given a collection of candidate numbers (candidates) and a target number
 * (target), find all unique combinations in candidates where the candidate
 * numbers sum to target.
 *
 * Each number in candidates may only be used once in the combination.
 *
 * Note: The solution set must not contain duplicate combinations.
 */
final class CombinationSum2 {

    /**
     * Find all unique combinations in candidates where the candidate numbers
     * sum to target.
     *
     * The time complexity is O(2^N) where N is the length of the candidates,
     * because there are 2 choices at every iteration
     *
     * The space complexity is O(N) as there will be N recursive calls where N
     * is the length of candidates.
     *
     * @param candidates The input array
     * @param target     The target integer
     * @return The results
     */
    public List<List<Integer>> combinationSum2(final int[] candidates,
            final int target) {

        if (candidates.length == 0 || candidates.length > 101 || target < 1
                || target > 30) {
            return Collections.emptyList();
        }

        List<List<Integer>> result = new ArrayList<>();
        // sorting allows us to stop the DFS early
        Arrays.sort(candidates);
        backtrack(candidates, target, result, new ArrayList<>(), 0);
        return result;
    }

    /**
     * Helper method implementing the backtracking.
     *
     * @param candidates The input array
     * @param target     The target integer
     * @param result     The results array containing proven candidates
     * @param list       The proposed candidate
     * @param start      The starting index for iterating over the candidates
     */
    private void backtrack(final int[] candidates, final int target,
            final List<List<Integer>> result, final List<Integer> list,
            final int start) {

        if (target < 0) {
            // the candidate did not meet the conditions
            return;
        } else if (target == 0) {
            // the candidate did meet the conditions
            result.add(new ArrayList<>(list));
            return;
        }

        for (int i = start; i < candidates.length; i++) {
            // rely on sorting to avoid duplicates
            if (i == start || candidates[i] != candidates[i - 1]) {
                // simulate taking the number
                list.add(candidates[i]);
                // pass in i+1 as we can't add the current number again
                backtrack(candidates, target - candidates[i], result, list,
                        i + 1);
                // simulate not taking the number
                list.remove(list.size() - 1);
            }
        }
    }
}
