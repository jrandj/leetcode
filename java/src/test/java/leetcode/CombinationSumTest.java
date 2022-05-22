package leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import junit.framework.TestCase;

public class CombinationSumTest extends TestCase {

    /**
     * The first test for CombinationSum.
     */
    public void testcombinationSum1() {
        int[] candidates = {2, 3, 6, 7};
        int target = 7;
        List<List<Integer>> testResult = new ArrayList<>();
        testResult.add(Arrays.asList(new Integer[] {2, 2, 3}));
        testResult.add(Arrays.asList(new Integer[] {7}));
        CombinationSum combinationSum = new CombinationSum();
        List<List<Integer>> output = combinationSum.combinationSum(candidates,
                target);
        assertEquals(output, testResult);
    }

    /**
     * The second test for CombinationSum.
     */
    public void testcombinationSum2() {
        int[] candidates = {2, 3, 5};
        int target = 8;
        List<List<Integer>> testResult = new ArrayList<>();
        testResult.add(Arrays.asList(new Integer[] {2, 2, 2, 2}));
        testResult.add(Arrays.asList(new Integer[] {2, 3, 3}));
        testResult.add(Arrays.asList(new Integer[] {3, 5}));
        CombinationSum combinationSum = new CombinationSum();
        List<List<Integer>> output = combinationSum.combinationSum(candidates,
                target);
        assertEquals(output, testResult);
    }

    /**
     * The third test for CombinationSum.
     */
    public void testcombinationSum3() {
        int[] candidates = {1};
        int target = 1;
        List<List<Integer>> testResult = new ArrayList<>();
        testResult.add(Arrays.asList(new Integer[] {1}));
        CombinationSum combinationSum = new CombinationSum();
        List<List<Integer>> output = combinationSum.combinationSum(candidates,
                target);
        assertEquals(output, testResult);
    }

    /**
     * The fourth test for CombinationSum.
     */
    public void testcombinationSum4() {
        int[] candidates = {1};
        int target = 2;
        List<List<Integer>> testResult = new ArrayList<>();
        testResult.add(Arrays.asList(new Integer[] {1, 1}));
        CombinationSum combinationSum = new CombinationSum();
        List<List<Integer>> output = combinationSum.combinationSum(candidates,
                target);
        assertEquals(output, testResult);
    }

}
