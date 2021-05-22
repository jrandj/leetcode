package leetcode;

/**
 * Given an array of non-negative integers nums, you are initially positioned at
 * the first index of the array.
 *
 * Each element in the array represents your maximum jump length at that
 * position.
 *
 * Determine if you are able to reach the last index.
 */
public class JumpGame {

    /**
     * Determine if you can reach the last index.
     *
     * The time complexity is O(2^N) as you make 2 decisions N times. Adding the
     * visited array reduces the time complexity to O(N^2) as for each element
     * you are iterating up to the farthest jump.
     *
     * The space complexity is O(N) for the recursive stack frames. Adding the
     * visited array adds O(N) space for the array, but O(2N) is still O(N).
     *
     * @param nums The input array.
     * @return True if you can and false if you cannot.
     */
    public boolean canJump(final int[] nums) {

        if (nums.length < 1 || nums.length > 10e5) {
            return false;
        }

        boolean[] visited = new boolean[nums.length];
        return canJumpFromPosition(nums, 0, visited);
    }

    /**
     * Helper method for recursion.
     *
     * @param nums     The input array.
     * @param position The current position.
     * @param visited  The array tracking the visited indices.
     * @return True if you can to the next position and false if you cannot.
     */
    private boolean canJumpFromPosition(final int[] nums, final int position,
            final boolean[] visited) {

        if (nums[position] > 10e5) {
            return false;
        }

        // we have reached the end
        if (position == nums.length - 1) {
            return true;
        }

        visited[position] = true;
        int furthestJump = nums[position];

        // do all of the jumps
        for (var i = 1; i <= furthestJump; i++) {

            if (!visited[position + i]
                    && canJumpFromPosition(nums, position + i, visited)) {
                return true;
            }
        }

        return false;
    }

    /**
     * Determine if you can reach the last index.
     *
     * The time complexity is O(N) as the array is traversed once.
     *
     * The space complexity is constant.
     *
     * @param nums The input array.
     * @return True if you can and false if you cannot.
     */
    public boolean canJumpGreedy(final int[] nums) {

        if (nums.length < 1 || nums.length > 10e5) {
            return false;
        }

        int lastGoodIndex = nums.length - 1;
        for (int i = nums.length - 1; i >= 0; i--) {
            // this means we can jump from nums[i] to the next good index
            if (nums[i] + i >= lastGoodIndex) {
                lastGoodIndex = i;
            }
        }

        return lastGoodIndex == 0;
    }

}
