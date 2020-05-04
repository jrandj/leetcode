package leetcode;

import java.util.Arrays;
import java.util.List;

import org.apache.commons.collections.CollectionUtils;

import junit.framework.Assert;
import junit.framework.TestCase;

public class GenerateParenthesesTest extends TestCase {
	public void testGenerateParenthesesTest1() {
		int n = 1;
		List<String> result = leetcode.GenerateParentheses.generateParenthesis(n);
		List<String> testResult = Arrays.asList("()");
		Assert.assertEquals(testResult, result);
	}
	
//	public void testGenerateParenthesesTest2() {
//		int n = 3;
//		List<String> result = leetcode.GenerateParentheses.generateParenthesis(n);
//		List<String> testResult = Arrays.asList("((()))", "(()())", "(())()", "()(())", "()()()");
//		Assert.assertEquals(testResult, result);
//	}
}