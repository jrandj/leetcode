package leetcode;

import org.junit.Assert;
import junit.framework.TestCase;

public class ClimbingStairsTest extends TestCase {

    /**
     * The first test for ClimbingStairs.
     */
    public void testClimbingStairs1() {
        int input = 2;
        int testResult = 2;
        ClimbingStairs climbingStairs = new ClimbingStairs();
        int output = climbingStairs.climbStairs(input);
        Assert.assertEquals(testResult, output);
    }

    /**
     * The second test for ClimbingStairs.
     */
    public void testClimbingStairs2() {
        int input = 3;
        int testResult = 3;
        ClimbingStairs climbingStairs = new ClimbingStairs();
        int output = climbingStairs.climbStairs(input);
        Assert.assertEquals(testResult, output);
    }

    /**
     * The third test for ClimbingStairs.
     */
    public void testClimbingStairs3() {
        int input = 4;
        int testResult = 5;
        ClimbingStairs climbingStairs = new ClimbingStairs();
        int output = climbingStairs.climbStairs(input);
        Assert.assertEquals(testResult, output);
    }

}
