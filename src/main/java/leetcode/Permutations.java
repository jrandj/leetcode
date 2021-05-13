package leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Given an array nums of distinct integers, return all the possible
 * permutations. You can return the answer in any order.
 */
final class Permutations {

    /**
     * Brute force approach to find all permutations of the input array.
     *
     * The time complexity is O(N*N!) as we loop over each element N, and
     * backtracking is then N!.
     *
     * The space complexity is O(N*N!).
     *
     * @param nums The input array.
     * @return All permutations.
     */
    public List<List<Integer>> permute(final int[] nums) {

        List<List<Integer>> permutations = new ArrayList<>();
        List<Integer> permutation = new ArrayList<>();

        // naive way to get a List<Integer> from int[]
        Integer[] boxedNums = new Integer[nums.length];
        for (int i = 0; i < nums.length; i++) {
            boxedNums[i] = nums[i];
        }
        List<Integer> remainingElements = new ArrayList<Integer>(
                Arrays.asList(boxedNums));

        recursiveHelper(permutations, remainingElements, permutation);
        return permutations;
    }

    /**
     * Helper method for recursion.
     *
     * @param remainingElements The remaining elements to permute.
     * @param permutations      All permutations.
     * @param permutation       The current permutation.
     */
    private void recursiveHelper(final List<List<Integer>> permutations,
            final List<Integer> remainingElements,
            final List<Integer> permutation) {

        // stop if we have used all of the remaining objects
        if (remainingElements.isEmpty()) {
            permutations.add(new ArrayList<>(permutation));
            return;
        }

        for (int i = 0; i < remainingElements.size(); i++) {
            int remainingElement = remainingElements.get(i);
            remainingElements.remove(i);
            permutation.add(remainingElement);
//            System.out.println("Permutation is: " + permutation.toString());
//            System.out.println(
//                    "Remaining elements are: " + remainingElements.toString());
            recursiveHelper(permutations, remainingElements, permutation);
            permutation.remove(Integer.valueOf(remainingElement));
            remainingElements.add(i, remainingElement);
//            System.out.println("Permutation is: " + permutation.toString());
//            System.out.println(
//                    "Remaining elements are: " + remainingElements.toString());
        }
    }

}
