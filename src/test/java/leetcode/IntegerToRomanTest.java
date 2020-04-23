package leetcode;

import junit.framework.TestCase;

public class IntegerToRomanTest extends TestCase {
	public void testintToRoman1() {
		String testResult = leetcode.IntegerToRoman.intToRoman(3);
		String actualResult = "III";
		assertEquals(testResult, actualResult);
	}

	public void testintToRoman2() {
		String testResult = leetcode.IntegerToRoman.intToRoman(4);
		String actualResult = "IV";
		assertEquals(testResult, actualResult);
	}

	public void testintToRoman3() {
		String testResult = leetcode.IntegerToRoman.intToRoman(9);
		String actualResult = "IX";
		assertEquals(testResult, actualResult);
	}

	public void testintToRoman4() {
		String testResult = leetcode.IntegerToRoman.intToRoman(58);
		String actualResult = "LVIII";
		assertEquals(testResult, actualResult);
	}

	public void testintToRoman5() {
		String testResult = leetcode.IntegerToRoman.intToRoman(1994);
		String actualResult = "MCMXCIV";
		assertEquals(testResult, actualResult);
	}

	public void testintToRoman6() {
		String testResult = leetcode.IntegerToRoman.intToRoman(40);
		String actualResult = "XL";
		assertEquals(testResult, actualResult);
	}

	public void testintToRoman7() {
		String testResult = leetcode.IntegerToRoman.intToRoman(400);
		String actualResult = "CD";
		assertEquals(testResult, actualResult);
	}

	public void testintToRoman8() {
		String testResult = leetcode.IntegerToRoman.intToRoman(450);
		String actualResult = "CDL";
		assertEquals(testResult, actualResult);
	}

	public void testintToRoman9() {
		String testResult = leetcode.IntegerToRoman.intToRoman(490);
		String actualResult = "CDXC";
		assertEquals(testResult, actualResult);
	}
}
