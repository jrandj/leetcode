package leetcode;

import junit.framework.TestCase;

public class RomanToIntegerTest extends TestCase {

    /**
     * The first test for RomanToInteger.
     */
    public void testRomanToInteger1() {
        int testResult = leetcode.RomanToInteger.romanToInt("III");
        int actualResult = 3;
        assertEquals(testResult, actualResult);
    }

    /**
     * The second test for RomanToInteger.
     */
    public void testRomanToInteger2() {
        int testResult = leetcode.RomanToInteger.romanToInt("IV");
        int actualResult = 4;
        assertEquals(testResult, actualResult);
    }

    /**
     * The third test for RomanToInteger.
     */
    public void testRomanToInteger3() {
        int testResult = leetcode.RomanToInteger.romanToInt("IX");
        int actualResult = 9;
        assertEquals(testResult, actualResult);
    }

    /**
     * The fourth test for RomanToInteger.
     */
    public void testRomanToInteger4() {
        int testResult = leetcode.RomanToInteger.romanToInt("LVIII");
        int actualResult = 58;
        assertEquals(testResult, actualResult);
    }

    /**
     * The fifth test for RomanToInteger.
     */
    public void testRomanToInteger5() {
        int testResult = leetcode.RomanToInteger.romanToInt("MCMXCIV");
        int actualResult = 1994;
        assertEquals(testResult, actualResult);
    }

}
