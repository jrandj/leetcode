package leetcode;

/**
 * Given an array of integers nums sorted in ascending order, find the starting
 * and ending position of a given target value.
 *
 * If target is not found in the array, return [-1, -1].
 *
 * Follow up: Could you write an algorithm with O(log n) runtime complexity?
 */
public final class FindFirstAndLastPositionOfElementInSortedArrray {

    FindFirstAndLastPositionOfElementInSortedArrray() {
        // prevent instantiation
    }

    /**
     * Find the starting and ending indices of the target.
     *
     * The time complexity is O(Log N) as it is binary search.
     *
     * The space complexity is constant.
     *
     * @param nums   the array of integers
     * @param target the target value
     * @return the first and last indices of the target value in the array
     */
    public int[] searchRange(final int[] nums, final int target) {

        if (nums.length < 0 || nums.length > 10e5 || target < -10e9
                || target > 10e9) {
            return new int[] {-1, -1};
        }

        int startingIndex = getStartingIndex(nums, target);
        int endingIndex = getEndingIndex(nums, target);
        return new int[] {startingIndex, endingIndex};
    }

    /**
     * Find the starting index of the target.
     *
     * The time complexity is O(Log N) as it is binary search.
     *
     * The space complexity is constant.
     *
     * @param nums   the array of integers
     * @param target the target value
     * @return the first index of the target value in the array
     */
    private int getStartingIndex(final int[] nums, final int target) {
        int left = 0;
        int right = nums.length - 1;
        int index = -1;
        while (left <= right) {
            int midPoint = (left + right) / 2;
            if (nums[midPoint] >= target) {
                right = midPoint - 1;
            } else {
                left = midPoint + 1;
            }
            if (nums[midPoint] == target) {
                index = midPoint;
            }
        }
        return index;
    }

    /**
     * Find the ending index of the target.
     *
     * The time complexity is O(Log N) as it is binary search.
     *
     * The space complexity is constant.
     *
     * @param nums   the array of integers
     * @param target the target value
     * @return the last index of the target value in the array
     */
    private int getEndingIndex(final int[] nums, final int target) {
        int left = 0;
        int right = nums.length - 1;
        int index = -1;

        while (left <= right) {
            int midPoint = (left + right) / 2;
            if (nums[midPoint] <= target) {
                left = midPoint + 1;
            } else {
                right = midPoint - 1;
            }
            if (nums[midPoint] == target) {
                index = midPoint;
            }
        }
        return index;
    }

}
