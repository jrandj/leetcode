package leetcode;

import junit.framework.TestCase;

public class ReverseIntegerTest extends TestCase {

    /**
     * The first test for ReverseInteger.
     */
    public void testReverseInteger1() {
        int result = 321;
        int input = 123;
        int output;
        output = leetcode.ReverseInteger.reverse(input);
        assertEquals(output, result);
    }

    /**
     * The second test for ReverseInteger.
     */
    public void testReverseInteger2() {
        int result = -123;
        int input = -321;
        int output;
        output = leetcode.ReverseInteger.reverse(input);
        System.out.println("output: " + output);
        System.out.print("result: " + result);
        assertEquals(output, result);
    }

    /**
     * The third test for ReverseInteger.
     */
    public void testReverseInteger3() {
        int result = 21;
        int input = 120;
        int output;
        output = leetcode.ReverseInteger.reverse(input);
        assertEquals(output, result);
    }

    /**
     * The fourth test for ReverseInteger.
     */
    public void testReverseInteger4() {
        int result = 0;
        int input = 0;
        int output;
        output = leetcode.ReverseInteger.reverse(input);
        assertEquals(output, result);
    }

    /**
     * The fifth test for ReverseInteger.
     */
    public void testReverseInteger5() {
        int result = 0;
        int input = 1534236469;
        int output;
        output = leetcode.ReverseInteger.reverse(input);
        assertEquals(output, result);
    }
}
