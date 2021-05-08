package leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import junit.framework.TestCase;

public class CombinationSum3Test extends TestCase {

    /**
     * The first test for CombinationSum3.
     */
    public void testcombinationSum3a() {
        int k = 3;
        int n = 7;
        List<List<Integer>> testResult = new ArrayList<>();
        testResult.add(Arrays.asList(new Integer[] {1, 2, 4}));
        CombinationSum3 combinationSum3 = new CombinationSum3();
        List<List<Integer>> output = combinationSum3.combinationSum3(k, n);
        assertEquals(output, testResult);
    }

    /**
     * The second test for CombinationSum3.
     */
    public void testcombinationSum3b() {
        int k = 3;
        int n = 9;
        List<List<Integer>> testResult = new ArrayList<>();
        testResult.add(Arrays.asList(new Integer[] {1, 2, 6}));
        testResult.add(Arrays.asList(new Integer[] {1, 3, 5}));
        testResult.add(Arrays.asList(new Integer[] {2, 3, 4}));
        CombinationSum3 combinationSum3 = new CombinationSum3();
        List<List<Integer>> output = combinationSum3.combinationSum3(k, n);
        assertEquals(output, testResult);
    }

    /**
     * The third test for CombinationSum3.
     */
    public void testcombinationSum3c() {
        int k = 3;
        int n = 2;
        List<List<Integer>> testResult = new ArrayList<>();

        CombinationSum3 combinationSum3 = new CombinationSum3();
        List<List<Integer>> output = combinationSum3.combinationSum3(k, n);
        assertEquals(output, testResult);
    }

    /**
     * The fourth test for CombinationSum3.
     */
    public void testcombinationSum3d() {
        int k = 9;
        int n = 45;
        List<List<Integer>> testResult = new ArrayList<>();
        testResult
                .add(Arrays.asList(new Integer[] {1, 2, 3, 4, 5, 6, 7, 8, 9}));
        CombinationSum3 combinationSum3 = new CombinationSum3();
        List<List<Integer>> output = combinationSum3.combinationSum3(k, n);
        assertEquals(output, testResult);
    }
}
