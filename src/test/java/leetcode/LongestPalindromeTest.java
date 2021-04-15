package leetcode;

import junit.framework.TestCase;

public class LongestPalindromeTest extends TestCase {

    /**
     * The first test for LongestPalindrome.
     */
    public void testlongestPalindrome1() {
        String myString = "babad";
        String testResult = "bab";
        String result = leetcode.LongestPalindrome
                .longestPalindromeSolution2(myString);
        assertEquals(testResult, result);
    }

    /**
     * The second test for LongestPalindrome.
     */
    public void testlongestPalindrome2() {
        String myString = "cbbd";
        String testResult = "bb";
        String result = leetcode.LongestPalindrome
                .longestPalindromeSolution2(myString);
        assertEquals(testResult, result);
    }

    /**
     * The third test for LongestPalindrome.
     */
    public void testlongestPalindrome3() {
        String myString = "";
        String testResult = "";
        String result = leetcode.LongestPalindrome
                .longestPalindromeSolution2(myString);
        assertEquals(testResult, result);
    }

    /**
     * The fourth test for LongestPalindrome.
     */
    public void testlongestPalindrome4() {
        String myString = "ac";
        String testResult = "a";
        String result = leetcode.LongestPalindrome
                .longestPalindromeSolution2(myString);
        assertEquals(testResult, result);
    }

    /**
     * The fifth test for LongestPalindrome.
     */
    public void testlongestPalindrome5() {
        String myString = "racecar";
        String testResult = "racecar";
        String result = leetcode.LongestPalindrome
                .longestPalindromeSolution2(myString);
        assertEquals(testResult, result);
    }

    /**
     * The sixth test for LongestPalindrome.
     */
    public void testlongestPalindrome6() {
        String myString = "racecar";
        String testResult = "racecar";
        String result = leetcode.LongestPalindrome
                .longestPalindromeSolution2(myString);
        assertEquals(testResult, result);
    }

    /**
     * The seventh test for LongestPalindrome.
     */
    public void testlongestPalindrome7() {
        String myString = "a";
        String testResult = "a";
        String result = leetcode.LongestPalindrome
                .longestPalindromeSolution2(myString);
        assertEquals(testResult, result);
    }

    /**
     * The eighth test for LongestPalindrome.
     */
    public void testlongestPalindrome8() {
        String myString = "abacdfgdcaba";
        String testResult = "aba";
        String result = leetcode.LongestPalindrome
                .longestPalindromeSolution2(myString);
        assertEquals(testResult, result);
    }

    /**
     * The ninth test for LongestPalindrome.
     */
    public void testlongestPalindrome9() {
        String myString = "ccc";
        String testResult = "ccc";
        String result = leetcode.LongestPalindrome
                .longestPalindromeSolution2(myString);
        assertEquals(testResult, result);
    }

    /**
     * The tenth test for LongestPalindrome.
     */
    public void testlongestPalindrome10() {
        String myString = "aaaa";
        String testResult = "aaaa";
        String result = leetcode.LongestPalindrome
                .longestPalindromeSolution2(myString);
        assertEquals(testResult, result);
    }

    /**
     * The eleventh test for LongestPalindrome.
     */
    public void testlongestPalindrome11() {
        String myString = "babaddtattarrattatddetartrateedredividerb";
        String testResult = "ddtattarrattatdd";
        String result = leetcode.LongestPalindrome
                .longestPalindromeSolution2(myString);
        assertEquals(testResult, result);
    }

}
