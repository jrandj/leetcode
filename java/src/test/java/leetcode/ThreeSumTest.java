package leetcode;

import java.util.List;
import org.apache.commons.collections.CollectionUtils;
import junit.framework.TestCase;

public class ThreeSumTest extends TestCase {

    /**
     * The first test for ThreeSum.
     */
    public void testthreeSum1() {
        int[] inputArray = {-1, 0, 1, 0};
        List<List<Integer>> result = leetcode.ThreeSum.threeSum(inputArray);
        List<List<Integer>> testResult = List.of(List.of(-1, 0, 1));
        assertTrue(CollectionUtils.isEqualCollection(testResult, result));
    }

    /**
     * The second test for ThreeSum.
     */
    public void testthreeSum2() {
        int[] inputArray = {-1, 0, 1, 2, -1, -4};
        List<List<Integer>> result = leetcode.ThreeSum.threeSum(inputArray);
        List<List<Integer>> testResult = List.of(List.of(-1, 0, 1),
                List.of(-1, -1, 2));
        assertTrue(CollectionUtils.isEqualCollection(testResult, result));
    }
}
