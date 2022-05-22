package leetcode;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * Find all valid combinations of k numbers that sum up to n such that the
 * following conditions are true:
 *
 * - Only numbers 1 through 9 are used. - Each number is used at most once.
 *
 * Return a list of all possible valid combinations. The list must not contain
 * the same combination twice, and the combinations may be returned in any
 * order.
 */
final class CombinationSum3 {

    /**
     * Find all valid combinations of k numbers that sum to n.
     *
     * The time complexity O(9^k) as there at most k recursive calls that
     * iterate over at most 9 options.
     *
     * The space complexity is O(k) as there at most k elements in the result.
     *
     * @param k The number of elements.
     * @param n The target sum.
     * @return The combinations of k that sum to n.
     */
    public List<List<Integer>> combinationSum3(final int k, final int n) {

        if (k < 2 || k > 9 || n < 1 || n > 60) {
            return Collections.emptyList();
        }

        List<List<Integer>> result = new ArrayList<>();
        backtrack(result, 1, new ArrayList<>(), k, n);
        return result;
    }

    /**
     * Helper method for backtracking.
     *
     * @param result    The result we are building.
     * @param index     The number from 1-9 we are looking at.
     * @param candidate A candidate for inclusion in the result.
     * @param k         The number of elements.
     * @param n         The target sum.
     */
    private void backtrack(final List<List<Integer>> result, final int index,
            final List<Integer> candidate, final int k, final int n) {

        // we have exceeded n so we discard the candidate
        if (n < 0) {
            return;
        }

        // we have met n and the size is correct so we keep the candidate
        if (n == 0 && candidate.size() == k) {
            result.add(new ArrayList<>(candidate));
            return;
        }

        for (int i = index; i <= 9; i++) {
            // simulate adding i to the next slot
            candidate.add(i);
            // attempt to find remaining slots
            backtrack(result, i + 1, candidate, k, n - i);
            // simulate not adding i to the next slot
            candidate.remove(candidate.size() - 1);
        }
    }
}
