package leetcode;

import java.util.Arrays;

/**
 * Given an array of non-negative integers nums, you are initially positioned at
 * the first index of the array.
 *
 * Each element in the array represents your maximum jump length at that
 * position.
 *
 * Your goal is to reach the last index in the minimum number of jumps.
 *
 * You can assume that you can always reach the last index.
 *
 */

public class JumpGame2 {

    /**
     * Return the smallest number of jumps to traverse the array.
     *
     * The time complexity is O(N^2) as we are doing 2 nested traversals.
     *
     * The space complexity is O(N) to store the DP array.
     *
     * @param nums The input array.
     * @return The number of jumps to traverse the array.
     */
    public int jump(final int[] nums) {

        if (nums.length < 1 || nums.length > 1000) {
            return 0;
        }

        int[] dp = new int[nums.length];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;

        // loop through all elements
        for (var i = 0; i < nums.length; i++) {

            if (nums[i] > 10e5) {
                return 0;
            }

            int reach = nums[i] + i;
            // for each element try all possible jumps but don't go past end
            for (var j = i + 1; j <= Math.min(reach, nums.length - 1); j++) {
                // only replace existing value if smaller
                dp[j] = Math.min(dp[i] + 1, dp[j]);
            }

        }
        return dp[nums.length - 1];
    }

    /**
     * Return the smallest number of jumps to traverse the array.
     *
     * The time complexity is O(N) as we iterate over the loop once.
     *
     * The space complexity is constant.
     *
     * @param nums The input array.
     * @return The number of jumps to traverse the array.
     */
    public int jumpGreedy(final int[] nums) {

        if (nums.length < 1 || nums.length > 1000) {
            return 0;
        }

        var r = 0;
        var furthest = 0;
        var result = 0;

        while (r < nums.length - 1) {
            for (int i = 0; i < r + 1; i++) {
                furthest = Math.max(furthest, i + nums[i]);

            }
            r = furthest;
            result++;
        }

        return result;
    }
}
