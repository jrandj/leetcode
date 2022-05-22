package leetcode;

import junit.framework.TestCase;

public class JumpGame2Test extends TestCase {

    /**
     * The first test for JumpGame2.
     */
    public void testJumpGame2a() {
        int[] nums = {2, 3, 1, 1, 4};
        int testResult = 2;
        JumpGame2 jumpGame2 = new JumpGame2();
        int actualResult = jumpGame2.jump(nums);
        assertEquals(testResult, actualResult);
    }

    /**
     * The second test for JumpGame2.
     */
    public void testJumpGame2b() {
        int[] nums = {2, 3, 0, 1, 4};
        int testResult = 2;
        JumpGame2 jumpGame2 = new JumpGame2();
        int actualResult = jumpGame2.jump(nums);
        assertEquals(testResult, actualResult);
    }

    /**
     * The third test for JumpGame2.
     */
    public void testJumpGame2c() {
        int[] nums = {2, 3, 1, 1, 4};
        int testResult = 2;
        JumpGame2 jumpGame2 = new JumpGame2();
        int actualResult = jumpGame2.jumpGreedy(nums);
        assertEquals(testResult, actualResult);
    }

    /**
     * The fourth test for JumpGame2.
     */
    public void testJumpGame2d() {
        int[] nums = {2, 3, 0, 1, 4};
        int testResult = 2;
        JumpGame2 jumpGame2 = new JumpGame2();
        int actualResult = jumpGame2.jumpGreedy(nums);
        assertEquals(testResult, actualResult);
    }

}
