package leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.stream.Collectors;

/**
 * Implement next permutation, which rearranges numbers into the
 * lexicographically next greater permutation of numbers.
 *
 * If such an arrangement is not possible, it must rearrange it as the lowest
 * possible order (i.e., sorted in ascending order).
 *
 * The replacement must be in place and use only constant extra memory.
 */
public class NextPermutation {

    /**
     * Rearranges an input array into the lexicographically next greater
     * permutation of numbers.
     *
     * @param nums The input array.
     */
    public void nextPermutation(int[] nums) {
        // find element for which all subsequent elements are descending
        // find smallest element in subsequent element and switch with element
        // reverse the order of the subsequent elements

        ArrayList<ArrayList<Integer>> allPermutations = new ArrayList<>();
        findAllPermutations(nums, allPermutations, 0);

        for (ArrayList<Integer> permutation : allPermutations) {
            System.out.println("permutation: " + permutation.toString());
        }

    }

    /**
     * Brute force approach to find all permutations of the input array.
     *
     * @param nums            The input array.
     * @param allPermutations All permutations.
     * @param index           The index of nums we are looking at.
     */
    private void findAllPermutations(final int[] nums,
            final ArrayList<ArrayList<Integer>> allPermutations,
            final int index) {

        // check if swapping is complete
        if (index == nums.length - 1) {
            // required to add an int[] to an ArrayList<ArrayList<Integer>>
            allPermutations.add((ArrayList<Integer>) Arrays.stream(nums).boxed()
                    .collect(Collectors.toList()));
            System.out.println("nums: " + Arrays.toString(nums));
            return;
        }

        for (int i = index; i < nums.length; i++) {
            // exchange elements of the array
            swap(nums, i, index);
            findAllPermutations(nums, allPermutations, index + 1);
            // exchange elements back to avoid repeated values
            swap(nums, index, i);
        }
    }

    /**
     * Helper method for swapping elements in an array.
     *
     * @param nums  The input array.
     * @param left  The first position in the swap.
     * @param right The second position in the swap.
     */
    private void swap(final int[] nums, final int left, final int right) {
        int temp = nums[left];
        nums[left] = nums[right];
        nums[right] = temp;
    }

}
