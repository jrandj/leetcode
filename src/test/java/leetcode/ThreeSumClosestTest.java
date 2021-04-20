package leetcode;

import junit.framework.TestCase;

public class ThreeSumClosestTest extends TestCase {

    /**
     * The first test for ThreeSumClosest.
     */
    public void testthreeSumClosest1() {
        int[] nums = {-1, 2, 1, -4};
        int target = 1;
        int result = leetcode.ThreeSumClosest.threeSumClosest(nums, target);
        int testResult = 2;
        assertEquals(testResult, result);
    }

    /**
     * The second test for ThreeSumClosest.
     */
    public void testthreeSumClosest2() {
        int[] nums = {1, 1, 1, 0};
        int target = -100;
        int result = leetcode.ThreeSumClosest.threeSumClosest(nums, target);
        int testResult = 2;
        assertEquals(testResult, result);
    }

    /**
     * The third test for ThreeSumClosest.
     */
    public void testthreeSumClosest3() {
        int[] nums = {0, 2, 1, -3};
        int target = 1;
        int result = leetcode.ThreeSumClosest.threeSumClosest(nums, target);
        int testResult = 0;
        assertEquals(testResult, result);
    }

    /**
     * The fourth test for ThreeSumClosest.
     */
    public void testthreeSumClosest4() {
        int[] nums = {1, 1, -1, -1, 3};
        int target = -1;
        int result = leetcode.ThreeSumClosest.threeSumClosest(nums, target);
        int testResult = -1;
        assertEquals(testResult, result);
    }
}
