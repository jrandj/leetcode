package leetcode;

import java.util.Arrays;
import java.util.List;

import org.apache.commons.collections.CollectionUtils;

import junit.framework.Assert;
import junit.framework.TestCase;

public class LetterCombinationsofaPhoneNumberTest extends TestCase {
    /**
     * The first test for LetterCombinationsofaPhoneNumber.
     */
    public void testLetterCombinationsofaPhoneNumber1() {
        String digits = "23";
        List<String> result = leetcode.LetterCombinationsofaPhoneNumber
                .letterCombinations(digits);
        List<String> testResult = Arrays.asList("ad", "ae", "af", "bd", "be",
                "bf", "cd", "ce", "cf");
        Assert.assertEquals("Verify same list",
                CollectionUtils.getCardinalityMap(testResult),
                CollectionUtils.getCardinalityMap(result));
    }

    /**
     * The second test for LetterCombinationsofaPhoneNumber.
     */
    public void testLetterCombinationsofaPhoneNumber2() {
        String digits = "2";
        List<String> result = leetcode.LetterCombinationsofaPhoneNumber
                .letterCombinations(digits);
        List<String> testResult = Arrays.asList("a", "b", "c");
        Assert.assertEquals("Verify same list",
                CollectionUtils.getCardinalityMap(testResult),
                CollectionUtils.getCardinalityMap(result));
    }

    /**
     * The third test for LetterCombinationsofaPhoneNumber.
     */
    public void testLetterCombinationsofaPhoneNumber3() {
        String digits = "234";
        List<String> result = leetcode.LetterCombinationsofaPhoneNumber
                .letterCombinations(digits);
        List<String> testResult = Arrays.asList("adg", "adh", "adi", "aeg",
                "aeh", "aei", "afg", "afh", "afi", "bdg", "bdh", "bdi", "beg",
                "beh", "bei", "bfg", "bfh", "bfi", "cdg", "cdh", "cdi", "ceg",
                "ceh", "cei", "cfg", "cfh", "cfi");
        Assert.assertEquals("Verify same list",
                CollectionUtils.getCardinalityMap(testResult),
                CollectionUtils.getCardinalityMap(result));
    }
}
