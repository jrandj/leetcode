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

        recursiveHelper(remainingElements, permutations, permutation);
        return permutations;
    }

    /**
     * Helper method for recursion.
     *
     * @param remainingElements The remaining elements to permute.
     * @param permutations      All permutations.
     * @param permutation       The current permutation.
     */
    private void recursiveHelper(List<Integer> remainingElements,
            List<List<Integer>> permutations, List<Integer> permutation) {

        if (remainingElements.isEmpty()) {
            permutations.add(new ArrayList<>(permutation));
            return;
        }

        for (int i = 0; i < remainingElements.size(); i++) {
            permutation.add(remainingElements.get(i));
            System.out.println("Permutation is: " + permutation.toString());
            remainingElements.remove(i);
            System.out.println(
                    "Remaining elements are: " + remainingElements.toString());
            recursiveHelper(remainingElements, permutations, permutation);
        }
    }

}
