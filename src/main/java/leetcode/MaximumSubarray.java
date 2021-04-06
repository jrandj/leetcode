package leetcode;

/**
 * Contains methods for calculating the maximum sum from any contiguous
 * sub-array.
 */
public class MaximumSubarray {
    /**
     * This is the naive approach iterating over every contiguous sub-array.
     *
     * @param nums the input array
     * @return sum the largest sum of any contiguous sub-array
     */
    public int maxSubArrayNaive(final int[] nums) {
        int sum = 0;
        int maxSum = 0;

        if (nums.length == 1) {
            return nums[0];
        }

        for (int i = 0; i < nums.length; i++) {
            sum = 0;
            sum += nums[i];
            for (int j = i + 1; j < nums.length; j++) {
                sum += nums[j];
                if (sum > maxSum) {
                    maxSum = sum;
                }
            }
        }

        return maxSum;
    }

    /**
     * This is the approach using Kadane's algorithm.
     *
     * @param nums the input array
     * @return sum the largest sum of any contiguous sub-array
     */
    public int maxSubArrayKadane(final int[] nums) {
        int currentSum = 0;
        int maxSum = 0;

        for (int i = 0; i < nums.length; i++) {
            currentSum += nums[i];
            if (currentSum < 0) {
                currentSum = 0;
            }
            maxSum = Math.max(currentSum, maxSum);
        }

        return maxSum;
    }

    /**
     * Find the maximum possible sum such that nums[m] is an element.
     *
     * @param nums the input array
     * @param l    the starting index of the sub-array
     * @param m    the middle index of the sub-array
     * @param r    the ending index of the sub-array
     * @return result the largest sum of any contiguous sub-array
     */
    public int maxCrossingSum(final int[] nums, final int l, final int m, final int r) {
        // elements on left of mid
        int leftCurrentSum = 0;
        int leftMaxSum = Integer.MIN_VALUE;
        for (int i = m; i >= l; i--) {
            leftCurrentSum += nums[i];
            if (leftCurrentSum > leftMaxSum) {
                leftMaxSum = leftCurrentSum;
            }
        }

        // elements on right of mid
        int rightCurrentSum = 0;
        int rightMaxSum = Integer.MIN_VALUE;
        for (int i = m + 1; i <= r; i++) {
            rightCurrentSum += nums[i];
            if (rightCurrentSum > rightMaxSum) {
                rightMaxSum = rightCurrentSum;
            }
        }

        return Math.max(leftMaxSum, Math.max(rightMaxSum, leftMaxSum + rightMaxSum));
    }

    /**
     * A helper method for the recursive approach.
     *
     * @param nums the input array
     * @param l    the left index
     * @param r    the right index
     * @return sum the largest sum of any contiguous sub-array
     */
    public int maxSubArrayHelper(final int[] nums, final int l, final int r) {

        if (l == r) {
            return nums[l];
        }

        int m = (l + r) / 2;

        return Math.max(maxSubArrayHelper(nums, l, m),
                Math.max(maxSubArrayHelper(nums, m + 1, r), maxCrossingSum(nums, l, m, r)));
    }

    /**
     * This is the recursive approach.
     *
     * @param nums the input array
     * @return sum the largest sum of any contiguous sub-array
     */
    public int maxSubArrayRecursive(final int[] nums) {

        int l = 0;
        int r = nums.length - 1;

        return maxSubArrayHelper(nums, l, r);
    }
}
