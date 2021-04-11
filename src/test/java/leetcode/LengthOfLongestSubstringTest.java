package leetcode;

import junit.framework.TestCase;

public class LengthOfLongestSubstringTest extends TestCase {
    /**
     * The first test for LengthOfLongestSubstring.
     *
     */
    public void testlengthOfLongestSubstring1() {
        String testString = "abcabcbb";
        int testResult = 3;
        int testOutput = leetcode.LengthOfLongestSubstring
                .lengthOfLongestSubstringSolution(testString);
        assertEquals(testOutput, testResult);
    }

    /**
     * The second test for LengthOfLongestSubstring.
     *
     */
    public void testlengthOfLongestSubstring2() {
        String testString = "bbbbb";
        int testResult = 1;
        int testOutput = leetcode.LengthOfLongestSubstring
                .lengthOfLongestSubstringSolution(testString);
        assertEquals(testOutput, testResult);
    }

    /**
     * The third test for LengthOfLongestSubstring.
     *
     */
    public void testlengthOfLongestSubstring3() {
        String testString = "pwwkew";
        int testResult = 3;
        int testOutput = leetcode.LengthOfLongestSubstring
                .lengthOfLongestSubstringSolution(testString);
        assertEquals(testOutput, testResult);
    }

    /**
     * The fourth test for LengthOfLongestSubstring.
     *
     */
    public void testlengthOfLongestSubstring4() {
        String testString = "aab";
        int testResult = 2;
        int testOutput = leetcode.LengthOfLongestSubstring
                .lengthOfLongestSubstringSolution(testString);
        assertEquals(testOutput, testResult);
    }

    /**
     * The fifth test for LengthOfLongestSubstring.
     *
     */
    public void testlengthOfLongestSubstring5() {
        String testString = "dvdf";
        int testResult = 3;
        int testOutput = leetcode.LengthOfLongestSubstring
                .lengthOfLongestSubstringSolution(testString);
        assertEquals(testOutput, testResult);
    }

    /**
     * The sixth test for LengthOfLongestSubstring.
     *
     */
    public void testlengthOfLongestSubstring6() {
        String testString = " ";
        int testResult = 1;
        int testOutput = leetcode.LengthOfLongestSubstring
                .lengthOfLongestSubstringSolution(testString);
        assertEquals(testOutput, testResult);
    }

    /**
     * The seventh test for LengthOfLongestSubstring.
     *
     */
    public void testlengthOfLongestSubstring7() {
        String testString = "";
        int testResult = 0;
        int testOutput = leetcode.LengthOfLongestSubstring
                .lengthOfLongestSubstringSolution(testString);
        assertEquals(testOutput, testResult);
    }

    /**
     * The eighth test for LengthOfLongestSubstring.
     *
     */
    public void testlengthOfLongestSubstring8() {
        String testString = "aa";
        int testResult = 1;
        int testOutput = leetcode.LengthOfLongestSubstring
                .lengthOfLongestSubstringSolution(testString);
        assertEquals(testOutput, testResult);
    }

    /**
     * The ninth test for LengthOfLongestSubstring.
     *
     */
    public void testlengthOfLongestSubstring9() {
        String testString = "au";
        int testResult = 2;
        int testOutput = leetcode.LengthOfLongestSubstring
                .lengthOfLongestSubstringSolution(testString);
        assertEquals(testOutput, testResult);
    }
}
