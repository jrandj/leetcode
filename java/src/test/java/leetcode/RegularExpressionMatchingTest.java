package leetcode;

import junit.framework.TestCase;

public class RegularExpressionMatchingTest extends TestCase {

    /**
     * The first test for RegularExpressionMatching.
     */
    public void testRegularExpressionMatching1() {
        Boolean result = false;
        String s = "aa";
        String p = "a";
        Boolean output = leetcode.RegularExpressionMatching.isMatch(s, p);
        assertEquals(output, result);
    }

    /**
     * The second test for RegularExpressionMatching.
     */
    public void testRegularExpressionMatching2() {
        Boolean result = true;
        String s = "aa";
        String p = "a*";
        Boolean output = leetcode.RegularExpressionMatching.isMatch(s, p);
        assertEquals(output, result);
    }

    /**
     * The third test for RegularExpressionMatching.
     */
    public void testRegularExpressionMatching3() {
        Boolean result = true;
        String s = "ab";
        String p = ".*";
        Boolean output = leetcode.RegularExpressionMatching.isMatch(s, p);
        assertEquals(output, result);
    }

    /**
     * The fourth test for RegularExpressionMatching.
     */
    public void testRegularExpressionMatching4() {
        Boolean result = true;
        String s = "aab";
        String p = "c*a*b";
        Boolean output = leetcode.RegularExpressionMatching.isMatch(s, p);
        assertEquals(output, result);
    }

    /**
     * The fifth test for RegularExpressionMatching.
     */
    public void testRegularExpressionMatching5() {
        Boolean result = false;
        String s = "mississippi";
        String p = "mis*is*p*.";
        Boolean output = leetcode.RegularExpressionMatching.isMatch(s, p);
        assertEquals(output, result);
    }

    /**
     * The sixth test for RegularExpressionMatching.
     */
    public void testRegularExpressionMatching6() {
        Boolean result = false;
        String s = "aab";
        String p = "c*";
        Boolean output = leetcode.RegularExpressionMatching.isMatch(s, p);
        assertEquals(output, result);
    }

    /**
     * The seventh test for RegularExpressionMatching.
     */
    public void testRegularExpressionMatching7() {
        Boolean result = true;
        String s = "mississippi";
        String p = "mis*is*ip*.";
        Boolean output = leetcode.RegularExpressionMatching.isMatch(s, p);
        assertEquals(output, result);
    }

    /**
     * The eighth test for RegularExpressionMatching.
     */
    public void testRegularExpressionMatching8() {
        Boolean result = false;
        String s = "abcd";
        String p = "d*";
        Boolean output = leetcode.RegularExpressionMatching.isMatch(s, p);
        assertEquals(output, result);
    }

}
