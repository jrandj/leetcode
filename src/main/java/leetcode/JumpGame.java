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
     * The time complexity is O(2^N) as you make 2 decisions N times.
     *
     * The space complexity is O(N) for the recursive stack frames.
     *
     * @param nums The input array.
     * @return True if you can and false if you cannot.
     */
    public boolean canJump(final int[] nums) {
        return canJumpFromPosition(nums, 0);
    }

    /**
     * Helper method for recursion.
     *
     * @param nums     The input array.
     * @param position The current position.
     * @return True if you can to the next position and false if you cannot.
     */
    private boolean canJumpFromPosition(final int[] nums, final int position) {

        // we have reached the end
        if (position == nums.length - 1) {
            return true;
        }

        int furthestJump = nums[position];

        // do all of the jumps
        for (var i = 1; i <= furthestJump; i++) {
            if (canJumpFromPosition(nums, position + i)) {
                return true;
            }
        }

        return false;
    }

}
