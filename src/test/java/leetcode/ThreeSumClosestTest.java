package leetcode;

import junit.framework.TestCase;

public class ThreeSumClosestTest extends TestCase {
	public void testthreeSumClosest1() {
		int[] nums = { -1, 2, 1, -4 };
		int target = 1;
		int result = leetcode.ThreeSumClosest.threeSumClosest(nums, target);
		int testResult = 2;
		assertEquals(testResult, result);
	}
}
