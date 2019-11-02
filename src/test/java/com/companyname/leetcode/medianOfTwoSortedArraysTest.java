package com.companyname.leetcode;

import java.util.Arrays;
import java.util.List;
import junit.framework.TestCase;

public class medianOfTwoSortedArraysTest extends TestCase {
  
  public void testfindMedianSortedArrays1() {
    int[] nums1 = {1, 3};
    int[] nums2 = {2};
    double testResult = 2.0;
    double result = com.companyname.leetcode.medianOfTwoSortedArrays.findMedianSortedArrays(nums1, nums2);
    assertEquals(testResult, result);
  }
  
  public void testfindMedianSortedArrays2() {
    int[] nums1 = {1, 2};
    int[] nums2 = {3, 4};
    double testResult = 2.5;
    double result = com.companyname.leetcode.medianOfTwoSortedArrays.findMedianSortedArrays(nums1, nums2);
    assertEquals(testResult, result);
  }

  public void testfindMedianSortedArrays3() {
    int[] nums1 = {};
    int[] nums2 = {1};
    double testResult =1.0;
    double result = com.companyname.leetcode.medianOfTwoSortedArrays.findMedianSortedArrays(nums1, nums2);
    assertEquals(testResult, result);
  }
  
  public void testfindMedianSortedArrays4() {
    int[] nums1 = {2};
    int[] nums2 = {};
    double testResult = 2.0;
    double result = com.companyname.leetcode.medianOfTwoSortedArrays.findMedianSortedArrays(nums1, nums2);
    assertEquals(testResult, result);
  }
  
  public void testfindMedianSortedArrays5() {
    int[] nums1 = {3};
    int[] nums2 = {-2,-1};
    double testResult = -1.0;
    double result = com.companyname.leetcode.medianOfTwoSortedArrays.findMedianSortedArrays(nums1, nums2);
    assertEquals(testResult, result);
  }
  
  public void testfindMedianSortedArrays6() {
    int[] nums1 = {1, 2, 3};
    int[] nums2 = {4, 10, 19};
    double testResult = 3.5;
    double result = com.companyname.leetcode.medianOfTwoSortedArrays.findMedianSortedArrays(nums1, nums2);
    assertEquals(testResult, result);
  }
  
  public void testfindMedianSortedArrays7() {
    int[] nums1 = {};
    int[] nums2 = {1, 2, 3};
    double testResult = 2;
    double result = com.companyname.leetcode.medianOfTwoSortedArrays.findMedianSortedArrays(nums1, nums2);
    assertEquals(testResult, result);
  }
}

// middle score is (1+3)/2 = 2.0
// middle score is 2
// median is (2+2)/2 = 2

// middle score is (1+2)/2 = 1.5
// middle score is (3+4)/2 = 3.5
// median is (1.5+3.5)/2 = 2.5

// middle score is 2
// middle score is 0
// median is 2/2 = 1

// middle score is 3
// middle score is (-2-1)/2 = -1.5
// median is (1.5)/2


