package leetcode;

import junit.framework.TestCase;

public class RomanToIntegerTest extends TestCase {
	public void testaddTwoNumbers1() {
		int testResult = leetcode.RomanToInteger.romanToInt("III");
		int actualResult = 3;
		assertEquals(testResult, actualResult);
	}

	public void testaddTwoNumbers2() {
		int testResult = leetcode.RomanToInteger.romanToInt("IV");
		int actualResult = 4;
		assertEquals(testResult, actualResult);
	}

	public void testaddTwoNumbers3() {
		int testResult = leetcode.RomanToInteger.romanToInt("IX");
		int actualResult = 9;
		assertEquals(testResult, actualResult);
	}

	public void testaddTwoNumbers4() {
		int testResult = leetcode.RomanToInteger.romanToInt("LVIII");
		int actualResult = 58;
		assertEquals(testResult, actualResult);
	}

	public void testaddTwoNumbers5() {
		int testResult = leetcode.RomanToInteger.romanToInt("MCMXCIV");
		int actualResult = 1994;
		assertEquals(testResult, actualResult);
	}

}
