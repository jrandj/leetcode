package leetcode;

import java.util.List;

import junit.framework.TestCase;

public class ThreeSumTest extends TestCase {
	public void testthreeSum1() {
		int[] inputArray = { -1, 0, 1, 2, -1, -4 };
		List<List<Integer>> result = leetcode.ThreeSum.threeSum(inputArray);
		List<List<Integer>> testResult = List.of(List.of(-1,0,1), List.of(-1,-1,2));
		assertEquals(testResult, result);
	}
}
