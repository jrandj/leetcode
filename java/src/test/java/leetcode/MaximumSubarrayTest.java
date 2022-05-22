package leetcode;

import junit.framework.TestCase;

/**
*
*/
public class MaximumSubarrayTest extends TestCase {
    /**
     * The first test for the naive method.
     */
    public void testMaximumSubarrayNaive1() {
        int[] input = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
        int result = 6;
        MaximumSubarray testObject = new MaximumSubarray();
        int output = testObject.maxSubArrayNaive(input);
        assertEquals(output, result);
    }

    /**
     * The second test for the naive method.
     */
    public void testMaximumSubarrayNaive2() {
        int[] input = {1};
        int result = 1;
        MaximumSubarray testObject = new MaximumSubarray();
        int output = testObject.maxSubArrayNaive(input);
        assertEquals(output, result);
    }

    /**
     * The third test for the naive method.
     */
    public void testMaximumSubarrayNaive3() {
        int[] input = {5, 4, -1, 7, 8};
        int result = 23;
        MaximumSubarray testObject = new MaximumSubarray();
        int output = testObject.maxSubArrayNaive(input);
        assertEquals(output, result);
    }

    /**
     * The first test for Kadane's method.
     */
    public void testMaximumSubarrayKadane1() {
        int[] input = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
        int result = 6;
        MaximumSubarray testObject = new MaximumSubarray();
        int output = testObject.maxSubArrayKadane(input);
        assertEquals(output, result);
    }

    /**
     * The second test for Kadane's method.
     */
    public void testMaximumSubarrayKadane2() {
        int[] input = {1};
        int result = 1;
        MaximumSubarray testObject = new MaximumSubarray();
        int output = testObject.maxSubArrayKadane(input);
        assertEquals(output, result);
    }

    /**
     * The third test for Kadane's method.
     */
    public void testMaximumSubarrayKadane3() {
        int[] input = {5, 4, -1, 7, 8};
        int result = 23;
        MaximumSubarray testObject = new MaximumSubarray();
        int output = testObject.maxSubArrayKadane(input);
        assertEquals(output, result);
    }

    /**
     * The first test for the recursive method.
     */
    public void testMaximumSubarrayRecursive1() {
        int[] input = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
        int result = 6;
        MaximumSubarray testObject = new MaximumSubarray();
        int output = testObject.maxSubArrayRecursive(input);
        assertEquals(output, result);
    }

    /**
     * The second test for the recursive method.
     */
    public void testMaximumSubarrayRecursive2() {
        int[] input = {1};
        int result = 1;
        MaximumSubarray testObject = new MaximumSubarray();
        int output = testObject.maxSubArrayRecursive(input);
        assertEquals(output, result);
    }

    /**
     * The third test for the recursive method.
     */
    public void testMaximumSubarrayRecursive3() {
        int[] input = {5, 4, -1, 7, 8};
        int result = 23;
        MaximumSubarray testObject = new MaximumSubarray();
        int output = testObject.maxSubArrayRecursive(input);
        assertEquals(output, result);
    }

}
