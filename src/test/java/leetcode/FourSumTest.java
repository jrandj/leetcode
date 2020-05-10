package leetcode;

import java.util.List;

import org.apache.commons.collections.CollectionUtils;

import junit.framework.Assert;
import junit.framework.TestCase;

public class FourSumTest extends TestCase {
	public void testGenerateParenthesesTest1() {
		int[] n = {1, 0, -1, 0, -2, 2};
		int target = 0;
		List<List<Integer>> result = leetcode.FourSum.fourSum(n, target);
		List<List<Integer>> testResult = List.of(List.of(-1,  0, 0, 1), List.of(-2, -1, 1, 2), List.of(-2,  0, 0, 2));		
		Assert.assertTrue(CollectionUtils.isEqualCollection(testResult, result));
	}

}