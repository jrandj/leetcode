package leetcode;

import junit.framework.Assert;
import junit.framework.TestCase;

public class ValidParenthesesTest extends TestCase {
//	public void testGenerateParenthesesTest1() {
//		String n = "()";
//		Boolean result = leetcode.ValidParentheses.isValid(n);
//		Boolean testResult = true;
//		Assert.assertEquals(testResult, result);
//	}

	public void testGenerateParenthesesTest2() {
		String n = "()[]{}";
		Boolean result = leetcode.ValidParentheses.isValid(n);
		Boolean testResult = true;
		Assert.assertEquals(testResult, result);
	}
//
//	public void testGenerateParenthesesTest3() {
//		String n = "(]";
//		Boolean result = leetcode.ValidParentheses.isValid(n);
//		Boolean testResult = true;
//		Assert.assertEquals(testResult, result);
//	}
//
//	public void testGenerateParenthesesTest4() {
//		String n = "([)]";
//		Boolean result = leetcode.ValidParentheses.isValid(n);
//		Boolean testResult = true;
//		Assert.assertEquals(testResult, result);
//	}
//
//	public void testGenerateParenthesesTest5() {
//		String n = "{[]}";
//		Boolean result = leetcode.ValidParentheses.isValid(n);
//		Boolean testResult = true;
//		Assert.assertEquals(testResult, result);
//	}
}