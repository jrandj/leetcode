package leetcode;

/**
 * There is an integer array nums sorted in ascending order (with distinct
 * values).
 *
 * Prior to being passed to your function, nums is rotated at an unknown pivot
 * index k (0 <= k < nums.length) such that the resulting array is [nums[k],
 * nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For
 * example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become
 * [4,5,6,7,0,1,2].
 *
 * Given the array nums after the rotation and an integer target, return the
 * index of target if it is in nums, or -1 if it is not in nums.
 */
public final class SearchInRotatedSortedArray {

    SearchInRotatedSortedArray() {
        // prevent instantiation
    }

    /**
     * Find the index of the target.
     *
     * The time complexity is O(N) as all elements in nums are checked.
     *
     * The space complexity is constant.
     *
     * @param nums   the rotated array
     * @param target the target value
     * @return the index of the target value in the rotated array
     */
    public int searchNaive(final int[] nums, final int target) {
        if (nums.length < 1 || nums.length > 5000 || target < -10e4
                || target > 10e4) {
            return -1;
        }

        int index = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] < -10e4 || nums[i] > 10e4) {
                return -1;
            }
            if (nums[i] == target) {
                return index;
            }
            index++;
        }
        return -1;
    }

    /**
     * Find the index of the target.
     *
     * The time complexity is O(Log N) as it is using binary search.
     *
     * The space complexity is constant.
     *
     * @param nums   the rotated array
     * @param target the target value
     * @return the index of the target value in the rotated array
     */
    public int searchMergeSort(final int[] nums, final int target) {
        if (nums.length < 1 || nums.length > 5000 || target < -10e4
                || target > 10e4) {
            return -1;
        }

        // find the starting index (smallest element in the array)
        int left = 0;
        int right = nums.length - 1;
        while (left < right) {
            int mid = (left + right) / 2;
            if (nums[mid] > nums[right]) {
                // you know mid is not the smallest element as nums[right] is
                // smaller, so set mid + 1
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        // left is now at the smallest index
        int start = left;

        // reset boundaries for regular binary search
        left = 0;
        right = nums.length - 1;
        if (target >= nums[start] && target <= nums[right]) {
            // the target is in the right half of the original array
            left = start;
        } else {
            // the target is in the left half of the original array
            right = start;
        }

        // standard binary search
        while (left <= right) {
            int midPoint = (left + right) / 2;
            if (nums[midPoint] > target) {
                right = midPoint - 1;
            } else if (nums[midPoint] < target) {
                left = midPoint + 1;
            } else {
                return midPoint;
            }
        }

        return -1;
    }

}
