package leetcode;

import java.util.Arrays;
import java.util.List;
import junit.framework.TestCase;
import org.junit.Assert;

public class GenerateParenthesesTest extends TestCase {
    /**
     * The first test for GenerateParentheses.
     */
    public void testGenerateParenthesesTest1() {
        int n = 1;
        List<String> result = leetcode.GenerateParentheses
                .generateParenthesis(n);
        List<String> testResult = Arrays.asList("()");
        Assert.assertEquals(testResult, result);
    }

    /**
     * The second test for GenerateParentheses.
     */
    public void testGenerateParenthesesTest2() {
        int n = 3;
        List<String> result = leetcode.GenerateParentheses
                .generateParenthesis(n);
        List<String> testResult = Arrays.asList("((()))", "(()())", "(())()",
                "()(())", "()()()");
        Assert.assertEquals(testResult, result);
    }
}
