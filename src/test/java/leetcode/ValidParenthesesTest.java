package leetcode;

import org.junit.Assert;
import junit.framework.TestCase;

public class ValidParenthesesTest extends TestCase {

    /**
     * The first test for ValidParentheses.
     */
    public void testGenerateParenthesesTest1() {
        String n = "()";
        Boolean result = leetcode.ValidParentheses.isValid(n);
        Boolean testResult = true;
        Assert.assertEquals(testResult, result);
    }

    /**
     * The second test for ValidParentheses.
     */
    public void testGenerateParenthesesTest2() {
        String n = "()[]{}";
        Boolean result = leetcode.ValidParentheses.isValid(n);
        Boolean testResult = true;
        Assert.assertEquals(testResult, result);
    }

    /**
     * The third test for ValidParentheses.
     */
    public void testGenerateParenthesesTest3() {
        String n = "(]";
        Boolean result = leetcode.ValidParentheses.isValid(n);
        Boolean testResult = false;
        Assert.assertEquals(testResult, result);
    }

    /**
     * The fourth test for ValidParentheses.
     */
    public void testGenerateParenthesesTest4() {
        String n = "([)]";
        Boolean result = leetcode.ValidParentheses.isValid(n);
        Boolean testResult = false;
        Assert.assertEquals(testResult, result);
    }

    /**
     * The fifth test for ValidParentheses.
     */
    public void testGenerateParenthesesTest5() {
        String n = "{[]}";
        Boolean result = leetcode.ValidParentheses.isValid(n);
        Boolean testResult = true;
        Assert.assertEquals(testResult, result);
    }

    /**
     * The sixth test for ValidParentheses.
     */
    public void testGenerateParenthesesTest6() {
        String n = "[";
        Boolean result = leetcode.ValidParentheses.isValid(n);
        Boolean testResult = false;
        Assert.assertEquals(testResult, result);
    }

    /**
     * The seventh test for ValidParentheses.
     */
    public void testGenerateParenthesesTest7() {
        String n = "((";
        Boolean result = leetcode.ValidParentheses.isValid(n);
        Boolean testResult = false;
        Assert.assertEquals(testResult, result);
    }

    /**
     * The eighth test for ValidParentheses.
     */
    public void testGenerateParenthesesTest8() {
        String n = "]";
        Boolean result = leetcode.ValidParentheses.isValid(n);
        Boolean testResult = false;
        Assert.assertEquals(testResult, result);
    }
}
