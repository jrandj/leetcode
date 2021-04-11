package leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Given an array nums of n integers and an integer target, are there elements
 * a, b, c, and d in nums such that a + b + c + d = target? Find all unique
 * quadruplets in the array which gives the sum of target.
 *
 * Note: The solution set must not contain duplicate quadruplets.
 */
final class FourSum {

    private FourSum() {
        // prevent instantiation
    }

    /**
     * Return valid 4sum solutions.
     *
     * @param nums   the input array
     * @param target the target
     * @return the list of valid 4sum solutions
     */
    public static List<List<Integer>> fourSum(final int[] nums,
            final int target) {
        List<List<Integer>> outputArray = new ArrayList<List<Integer>>();

        if (nums == null || nums.length < 4) {
            return outputArray;
        }

        Arrays.sort(nums);

        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                int lp = j + 1;
                int rp = nums.length - 1;
                while (lp < rp) {
                    if (nums[i] + nums[j] + nums[lp] + nums[rp] == target) {
                        outputArray.add(Arrays.asList(nums[i], nums[j],
                                nums[lp], nums[rp]));

                        // skip duplicates
                        while (rp < nums.length - 1
                                && nums[lp] == nums[lp + 1]) {
                            lp++;
                        }
                        while (lp < rp + 1 && nums[rp] == nums[rp - 1]) {
                            rp--;
                        }
                        rp--;
                        lp++;

                    } else if (nums[i] + nums[j] + nums[lp]
                            + nums[rp] > target) {
                        rp--;
                    } else if (nums[i] + nums[j] + nums[lp]
                            + nums[rp] < target) {
                        lp++;
                    }
                }

                // skip duplicates
                while (j < nums.length - 1 && nums[j] == nums[j + 1]) {
                    j++;
                }
            }

            // skip duplicates
            while (i < nums.length - 1 && nums[i] == nums[i + 1]) {
                i++;
            }
        }
        return outputArray;
    }
}
