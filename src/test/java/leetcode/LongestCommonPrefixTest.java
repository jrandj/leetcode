package leetcode;

import junit.framework.TestCase;

public class LongestCommonPrefixTest extends TestCase {
	public void longestCommonPrefix1() {
		String[] inputArray = { "flower", "flow", "flight" };
		String testResult = leetcode.LongestCommonPrefix.longestCommonPrefix(inputArray);
		String actualResult = "fl";
		assertEquals(testResult, actualResult);
	}

	public void longestCommonPrefix2() {
		String[] inputArray = { "dog", "racecar", "car" };
		String testResult = leetcode.LongestCommonPrefix.longestCommonPrefix(inputArray);
		String actualResult = "";
		assertEquals(testResult, actualResult);
	}

	public void longestCommonPrefix3() {
		String[] inputArray = { "" };
		String testResult = leetcode.LongestCommonPrefix.longestCommonPrefix(inputArray);
		String actualResult = "";
		assertEquals(testResult, actualResult);
	}
}
