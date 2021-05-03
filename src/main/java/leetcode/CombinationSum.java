package leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

/**
 * Given an array of distinct integers candidates and a target integer target,
 * return a list of all unique combinations of candidates where the chosen
 * numbers sum to target. You may return the combinations in any order.
 *
 * The same number may be chosen from candidates an unlimited number of times.
 * Two combinations are unique if the frequency of at least one of the chosen
 * numbers is different.
 *
 * It is guaranteed that the number of unique combinations that sum up to target
 * is less than 150 combinations for the given input.
 */
final class CombinationSum {

    CombinationSum() {
        // prevent instantiation
    }

    /**
     * Find a list of unique combinations of candidates where the chosen numbers
     * sum to target.
     *
     * The time complexity is O(N^target) with N the length of the candidates
     * array.
     *
     * The space complexity is O(target).
     *
     * @param candidates The input array
     * @param target     The target integer
     * @return The results
     */
    public List<List<Integer>> combinationSum(final int[] candidates,
            final int target) {

        if (candidates.length < 1 || candidates.length > 30 || target < 1
                || target > 500) {
            return Collections.emptyList();
        }

        Arrays.sort(candidates);
        List<List<Integer>> result = new ArrayList<>();
        backtrack(candidates, 0, target, new ArrayList<>(), result);
        return result;
    }

    /**
     * Helper method implementing the backtracking.
     *
     * @param candidates The input array
     * @param start      The starting index
     * @param target     The target integer
     * @param list       The temporary list of results
     * @param result     A result
     */
    private void backtrack(final int[] candidates, final int start,
            final int target, final List<Integer> list,
            final List<List<Integer>> result) {

        // If a result is found add it to the result
        if (target < 0) {
            return;
        } else if (target == 0) {
            result.add(new ArrayList<>(list));
            return;
        }

        for (int i = start; i < candidates.length; i++) {
            // Take advantage of a sorted candidates array
            if (candidates[i] > target) {
                return;
            }
            list.add(candidates[i]);
            backtrack(candidates, i, target - candidates[i], list, result);
            list.remove(list.size() - 1);
        }
    }
}
