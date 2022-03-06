package leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import junit.framework.TestCase;

public class CombinationSum2Test extends TestCase {

    /**
     * The first test for CombinationSum2.
     */
    public void testcombinationSum2a() {
        int[] candidates = {10, 1, 2, 7, 6, 1, 5};
        int target = 8;
        List<List<Integer>> testResult = new ArrayList<>();
        testResult.add(Arrays.asList(new Integer[] {1, 1, 6}));
        testResult.add(Arrays.asList(new Integer[] {1, 2, 5}));
        testResult.add(Arrays.asList(new Integer[] {1, 7}));
        testResult.add(Arrays.asList(new Integer[] {2, 6}));
        CombinationSum2 combinationSum2 = new CombinationSum2();
        List<List<Integer>> output = combinationSum2.combinationSum2(candidates,
                target);
        assertEquals(output, testResult);
    }

    /**
     * The second test for CombinationSum2.
     */
    public void testcombinationSum2b() {
        int[] candidates = {2, 5, 2, 1, 2};
        int target = 5;
        List<List<Integer>> testResult = new ArrayList<>();
        testResult.add(Arrays.asList(new Integer[] {1, 2, 2}));
        testResult.add(Arrays.asList(new Integer[] {5}));
        CombinationSum2 combinationSum2 = new CombinationSum2();
        List<List<Integer>> output = combinationSum2.combinationSum2(candidates,
                target);
        assertEquals(output, testResult);
    }
}
