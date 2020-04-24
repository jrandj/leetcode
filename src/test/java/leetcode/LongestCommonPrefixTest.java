package leetcode;

import junit.framework.TestCase;

public class LongestCommonPrefixTest extends TestCase {
//	public void testlongestCommonPrefix1() {
//		String[] inputArray = { "flower", "flow", "flight" };
//		String testResult = leetcode.LongestCommonPrefix.longestCommonPrefix(inputArray);
//		String actualResult = "fl";
//		assertEquals(testResult, actualResult);
//	}
//
//	public void testlongestCommonPrefix2() {
//		String[] inputArray = { "dog", "racecar", "car" };
//		String testResult = leetcode.LongestCommonPrefix.longestCommonPrefix(inputArray);
//		String actualResult = "";
//		assertEquals(testResult, actualResult);
//	}
//
//	public void testlongestCommonPrefix3() {
//		String[] inputArray = { "" };
//		String testResult = leetcode.LongestCommonPrefix.longestCommonPrefix(inputArray);
//		String actualResult = "";
//		assertEquals(testResult, actualResult);
//	}
//
//	public void testlongestCommonPrefix4() {
//		String[] inputArray = { "", "b" };
//		String testResult = leetcode.LongestCommonPrefix.longestCommonPrefix(inputArray);
//		String actualResult = "";
//		assertEquals(testResult, actualResult);
//	}
//	
//	public void testlongestCommonPrefix5() {
//		String[] inputArray = { "c", "c" };
//		String testResult = leetcode.LongestCommonPrefix.longestCommonPrefix(inputArray);
//		String actualResult = "c";
//		assertEquals(testResult, actualResult);
//	}
//	
//	public void testlongestCommonPrefix6() {
//		String[] inputArray = { "aaa","aa","aaa" };
//		String testResult = leetcode.LongestCommonPrefix.longestCommonPrefix(inputArray);
//		String actualResult = "aa";
//		assertEquals(testResult, actualResult);
//	}
	
	public void testlongestCommonPrefix7() {
		String[] inputArray = { "abca","abc" };
		String testResult = leetcode.LongestCommonPrefix.longestCommonPrefix(inputArray);
		String actualResult = "abc";
		assertEquals(testResult, actualResult);
	}
}
