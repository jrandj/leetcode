package leetcode;

import org.junit.Assert;
import junit.framework.TestCase;

public class SortColorsTest extends TestCase {

    /**
     * The first test for SortColors.
     */
    public void testSortColors() {
        int[] testResult = {0, 0, 1, 1, 2, 2};
        int[] input = {2, 0, 2, 1, 1, 0};
        SortColors sortColorsTest = new SortColors();
        sortColorsTest.sortColors(input);
        Assert.assertArrayEquals(input, testResult);
    }

}
