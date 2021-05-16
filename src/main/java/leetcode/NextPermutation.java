package leetcode;

import java.util.Arrays;

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
     * Rearrange the input array into the lexicographically next greatest
     * number.
     *
     * The time complexity is O(N) as we are doing linear operations on the
     * input array. Sorting complexity is additional and not multiplicative so
     * is not included in the time complexity.
     *
     * The space complexity is constant.
     *
     * @param nums The input array.
     */
    public void nextPermutation(final int[] nums) {

        if (nums.length > 100 || nums.length < 1) {
            return;
        }

        for (int i = nums.length - 1; i > 0; i--) {

            if (nums[i] < 0 || nums[i] > 100) {
                return;
            }

            if (nums[i] > nums[i - 1]) {
                Arrays.sort(nums, i, nums.length);
                for (int p = i - 1; p < nums.length - 1; p++) {
                    // find first element larger than nums[i - 1]
                    if (nums[p + 1] > nums[i - 1]) {
                        // swap elements
                        int temp = nums[p + 1];
                        nums[p + 1] = nums[i - 1];
                        nums[i - 1] = temp;
                        return;
                    }
                }
            }
        }

        // handle if array was sorted in descending order
        Arrays.sort(nums, 0, nums.length);
    }

}
