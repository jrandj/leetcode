package leetcode;

import java.util.Arrays;
import java.util.List;

import org.apache.commons.collections.CollectionUtils;

import junit.framework.Assert;
import junit.framework.TestCase;

public class LetterCombinationsofaPhoneNumberTest extends TestCase {
	public void testthreeSumClosest1() {
		String digits = "23";
		List<String> result = leetcode.LetterCombinationsofaPhoneNumber.letterCombinations(digits);
		List<String> testResult = Arrays.asList("ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf");
		Assert.assertEquals("Verify same list", CollectionUtils.getCardinalityMap(testResult),
				CollectionUtils.getCardinalityMap(result));
	}

	public void testthreeSumClosest2() {
		String digits = "2";
		List<String> result = leetcode.LetterCombinationsofaPhoneNumber.letterCombinations(digits);
		List<String> testResult = Arrays.asList("a", "b", "c");
		Assert.assertEquals("Verify same list", CollectionUtils.getCardinalityMap(testResult),
				CollectionUtils.getCardinalityMap(result));
	}

}