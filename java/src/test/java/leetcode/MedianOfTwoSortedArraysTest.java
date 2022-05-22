package leetcode;

import junit.framework.TestCase;

public class MedianOfTwoSortedArraysTest extends TestCase {

    /**
     * The first test for MedianOfTwoSortedArrays.
     */
    public void testfindMedianSortedArrays1() {
        int[] nums1 = {1, 3};
        int[] nums2 = {2};
        double testResult = 2.0;
        double result = leetcode.MedianOfTwoSortedArrays
                .findMedianSortedArrays(nums1, nums2);
        assertEquals(testResult, result);
    }

    /**
     * The second test for MedianOfTwoSortedArrays.
     */
    public void testfindMedianSortedArrays2() {
        int[] nums1 = {1, 2};
        int[] nums2 = {3, 4};
        double testResult = 2.5;
        double result = leetcode.MedianOfTwoSortedArrays
                .findMedianSortedArrays(nums1, nums2);
        assertEquals(testResult, result);
    }

    /**
     * The third test for MedianOfTwoSortedArrays.
     */
    public void testfindMedianSortedArrays3() {
        int[] nums1 = {};
        int[] nums2 = {1};
        double testResult = 1.0;
        double result = leetcode.MedianOfTwoSortedArrays
                .findMedianSortedArrays(nums1, nums2);
        assertEquals(testResult, result);
    }

    /**
     * The fourth test for MedianOfTwoSortedArrays.
     */
    public void testfindMedianSortedArrays4() {
        int[] nums1 = {2};
        int[] nums2 = {};
        double testResult = 2.0;
        double result = leetcode.MedianOfTwoSortedArrays
                .findMedianSortedArrays(nums1, nums2);
        assertEquals(testResult, result);
    }

    /**
     * The fifth test for MedianOfTwoSortedArrays.
     */
    public void testfindMedianSortedArrays5() {
        int[] nums1 = {3};
        int[] nums2 = {-2, -1};
        double testResult = -1.0;
        double result = leetcode.MedianOfTwoSortedArrays
                .findMedianSortedArrays(nums1, nums2);
        assertEquals(testResult, result);
    }

    /**
     * The sixth test for MedianOfTwoSortedArrays.
     */
    public void testfindMedianSortedArrays6() {
        int[] nums1 = {1, 2, 3};
        int[] nums2 = {4, 10, 19};
        double testResult = 3.5;
        double result = leetcode.MedianOfTwoSortedArrays
                .findMedianSortedArrays(nums1, nums2);
        assertEquals(testResult, result);
    }

    /**
     * The seventh test for MedianOfTwoSortedArrays.
     */
    public void testfindMedianSortedArrays7() {
        int[] nums1 = {};
        int[] nums2 = {1, 2, 3};
        double testResult = 2;
        double result = leetcode.MedianOfTwoSortedArrays
                .findMedianSortedArrays(nums1, nums2);
        assertEquals(testResult, result);
    }
}
