package leetcode;

/**
 * There are two sorted arrays nums1 and nums2 of size m and n respectively.
 * Find the median of the two sorted arrays. The overall run time complexity
 * should be O(log (m+n)). You may assume nums1 and nums2 cannot be both empty.
 */
public final class MedianOfTwoSortedArrays {

    private MedianOfTwoSortedArrays() {
        // prevent instantiation
    }

    /**
     * This is the naive approach iterating over every contiguous sub-array.
     *
     * @param nums1 the first sub-array
     * @param nums2 the second sub-array
     * @param i     the first index
     * @param j     the second index
     * @param k     the third index
     * @return the median
     */
    private static double getKthSmallest(final int[] nums1, final int[] nums2,
            final int i, final int j, final int k) {

        // out of bounds for nums1 as max index is nums1.length - 1 we already
        // came in with k as the middle value, if nums1 is empty it's just the
        // middle value of nums2
        if (i == nums1.length) {
            return nums2[j + k];
        } else if (j == nums2.length) {
            return nums1[i + k];
        } else if (k == 0) {
            return Math.min(nums1[i], nums2[j]);
        }
        // catch out of bound indices
        int midNums1Idx = Math.min((k + 1) / 2, nums1.length - i);
        int midNums2Idx = Math.min((k + 1) / 2, nums2.length - j);

        // middle value of search space for nums1 and nums2
        int midNums1 = nums1[i + midNums1Idx - 1];
        int midNums2 = nums2[j + midNums2Idx - 1];

        // if midNums2 > midNums1 there are at least k elements greater than
        // midNums1 in nums2
        if (midNums2 > midNums1) {
            return getKthSmallest(nums1, nums2, i + midNums1Idx, j,
                    k - midNums1Idx);
        } else {
            return getKthSmallest(nums1, nums2, i, j + midNums2Idx,
                    k - midNums2Idx);
        }

    }

    /**
     * This is the naive approach iterating over every contiguous sub-array.
     *
     * @param nums1 the first sub-array
     * @param nums2 the second sub-array
     * @return the median
     */
    public static double findMedianSortedArrays(final int[] nums1,
            final int[] nums2) {
        // Find combined length of nums1 and nums2
        int n = nums1.length + nums2.length;
        // if n is odd just use middle number
        if (n % 2 != 0) {
            return getKthSmallest(nums1, nums2, 0, 0, n / 2); // e.g. 3/2 = 1
            // if n is even need to average middle 2 numbers
        } else {
            double firstNumber = getKthSmallest(nums1, nums2, 0, 0, n / 2 - 1);
            double secondNumber = getKthSmallest(nums1, nums2, 0, 0, n / 2);
            return (firstNumber + secondNumber) / 2.0;
        }
    }
}
