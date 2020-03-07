package leetcode;

import junit.framework.TestCase;

public class MedianOfTwoSortedArraysTest extends TestCase {

  public void testfindMedianSortedArrays1() {
    int[] nums1 = {1, 3};
    int[] nums2 = {2};
    double testResult = 2.0;
    double result = leetcode.MedianOfTwoSortedArrays.findMedianSortedArrays(nums1, nums2);
    assertEquals(testResult, result);
  }

  public void testfindMedianSortedArrays2() {
    int[] nums1 = {1, 2};
    int[] nums2 = {3, 4};
    double testResult = 2.5;
    double result = leetcode.MedianOfTwoSortedArrays.findMedianSortedArrays(nums1, nums2);
    assertEquals(testResult, result);
  }

  public void testfindMedianSortedArrays3() {
    int[] nums1 = {};
    int[] nums2 = {1};
    double testResult = 1.0;
    double result = leetcode.MedianOfTwoSortedArrays.findMedianSortedArrays(nums1, nums2);
    assertEquals(testResult, result);
  }

  public void testfindMedianSortedArrays4() {
    int[] nums1 = {2};
    int[] nums2 = {};
    double testResult = 2.0;
    double result = leetcode.MedianOfTwoSortedArrays.findMedianSortedArrays(nums1, nums2);
    assertEquals(testResult, result);
  }

  public void testfindMedianSortedArrays5() {
    int[] nums1 = {3};
    int[] nums2 = {-2, -1};
    double testResult = -1.0;
    double result = leetcode.MedianOfTwoSortedArrays.findMedianSortedArrays(nums1, nums2);
    assertEquals(testResult, result);
  }

  public void testfindMedianSortedArrays6() {
    int[] nums1 = {1, 2, 3};
    int[] nums2 = {4, 10, 19};
    double testResult = 3.5;
    double result = leetcode.MedianOfTwoSortedArrays.findMedianSortedArrays(nums1, nums2);
    assertEquals(testResult, result);
  }

  public void testfindMedianSortedArrays7() {
    int[] nums1 = {};
    int[] nums2 = {1, 2, 3};
    double testResult = 2;
    double result = leetcode.MedianOfTwoSortedArrays.findMedianSortedArrays(nums1, nums2);
    assertEquals(testResult, result);
  }
}


