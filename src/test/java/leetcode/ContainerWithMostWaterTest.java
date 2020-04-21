package leetcode;

import junit.framework.TestCase;

public class ContainerWithMostWaterTest extends TestCase {
	public void testaddTwoNumbers1() {
		int[] inputArray = { 1, 8, 6, 2, 5, 4, 8, 3, 7 };
		int testResult = leetcode.ContainerWithMostWater.maxArea(inputArray);
		int actualResult = 49;
		assertEquals(testResult, actualResult);
	}
}
