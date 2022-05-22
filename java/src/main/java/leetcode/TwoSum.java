package leetcode;

/**
 * Given an array of integers, return indices of the two numbers such that they
 * add up to a specific target. You may assume that each input would have
 * exactly one solution, and you may not use the same element twice.
 */
public final class TwoSum {

    private TwoSum() {
        // prevent instantiation
    }

    /**
     * Return unique triplets that sum to zero.
     *
     * @param nums   the array of ints
     * @param target the target int
     * @return indices of nums that add up to the target
     */
    public static int[] twoSumSolution(final int[] nums, final int target) {
        for (int i = 0; i < (nums.length); i++) {
            for (int j = 0; j < (nums.length); j++) {
                if (nums[i] + nums[j] == target && i != j) {
                    return new int[] {i, j};
                }
            }
        }
        return new int[0];
    }
}
