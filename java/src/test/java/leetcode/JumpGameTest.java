package leetcode;

import junit.framework.TestCase;

public class JumpGameTest extends TestCase {

    /**
     * The first test for Jump Game.
     */
    public void testJumpGameTest1() {
        int[] input = new int[] {2, 3, 1, 1, 4};
        boolean testResult = true;
        JumpGame jumpGame = new JumpGame();
        boolean output = jumpGame.canJump(input);
        assertEquals(output, testResult);
    }

    /**
     * The second test for Jump Game.
     */
    public void testJumpGameTest2() {
        int[] input = new int[] {3, 2, 1, 0, 4};
        boolean testResult = false;
        JumpGame jumpGame = new JumpGame();
        boolean output = jumpGame.canJump(input);
        assertEquals(output, testResult);
    }

    /**
     * The third test for Jump Game.
     */
    public void testJumpGameTest3() {
        int[] input = new int[] {2, 3, 1, 1, 4};
        boolean testResult = true;
        JumpGame jumpGame = new JumpGame();
        boolean output = jumpGame.canJumpGreedy(input);
        assertEquals(output, testResult);
    }

    /**
     * The fourth test for Jump Game.
     */
    public void testJumpGameTest4() {
        int[] input = new int[] {3, 2, 1, 0, 4};
        boolean testResult = false;
        JumpGame jumpGame = new JumpGame();
        boolean output = jumpGame.canJumpGreedy(input);
        assertEquals(output, testResult);
    }

}
