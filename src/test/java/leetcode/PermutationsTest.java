package leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import junit.framework.TestCase;

public class PermutationsTest extends TestCase {

    /**
     * The first test for Permutations.
     */
    public void testPermutations1() {
        int[] nums = {1, 2, 3};
        List<List<Integer>> testResult = new ArrayList<>();
        testResult.add(Arrays.asList(new Integer[] {1, 2, 3}));
        testResult.add(Arrays.asList(new Integer[] {1, 3, 2}));
        testResult.add(Arrays.asList(new Integer[] {2, 1, 3}));
        testResult.add(Arrays.asList(new Integer[] {2, 3, 1}));
        testResult.add(Arrays.asList(new Integer[] {3, 1, 2}));
        testResult.add(Arrays.asList(new Integer[] {3, 2, 1}));
        Permutations permutations = new Permutations();
        List<List<Integer>> output = permutations.permute(nums);
        assertTrue(output.size() == testResult.size()
                && output.containsAll(testResult)
                && testResult.containsAll(output));
    }

    /**
     * The second test for Permutations.
     */
    public void testPermutations2() {
        int[] nums = {0, 1};
        List<List<Integer>> testResult = new ArrayList<>();
        testResult.add(Arrays.asList(new Integer[] {0, 1}));
        testResult.add(Arrays.asList(new Integer[] {1, 0}));
        Permutations permutations = new Permutations();
        List<List<Integer>> output = permutations.permute(nums);
        assertTrue(output.size() == testResult.size()
                && output.containsAll(testResult)
                && testResult.containsAll(output));
    }

    /**
     * The third test for Permutations.
     */
    public void testPermutations3() {
        int[] nums = {1};
        List<List<Integer>> testResult = new ArrayList<>();
        testResult.add(Arrays.asList(new Integer[] {1}));
        Permutations permutations = new Permutations();
        List<List<Integer>> output = permutations.permute(nums);
        assertTrue(output.size() == testResult.size()
                && output.containsAll(testResult)
                && testResult.containsAll(output));
    }

    /**
     * The fourth test for Permutations.
     */
    public void testPermutations4() {
        int[] nums = {1, 2, 3};
        List<List<Integer>> testResult = new ArrayList<>();
        testResult.add(Arrays.asList(new Integer[] {1, 2, 3}));
        testResult.add(Arrays.asList(new Integer[] {1, 3, 2}));
        testResult.add(Arrays.asList(new Integer[] {2, 1, 3}));
        testResult.add(Arrays.asList(new Integer[] {2, 3, 1}));
        testResult.add(Arrays.asList(new Integer[] {3, 1, 2}));
        testResult.add(Arrays.asList(new Integer[] {3, 2, 1}));
        Permutations permutations = new Permutations();
        List<List<Integer>> output = permutations.permuteHeapsAlgorithm(nums);
        assertTrue(output.size() == testResult.size()
                && output.containsAll(testResult)
                && testResult.containsAll(output));
    }

    /**
     * The fifth test for Permutations.
     */
    public void testPermutations5() {
        int[] nums = {0, 1};
        List<List<Integer>> testResult = new ArrayList<>();
        testResult.add(Arrays.asList(new Integer[] {0, 1}));
        testResult.add(Arrays.asList(new Integer[] {1, 0}));
        Permutations permutations = new Permutations();
        List<List<Integer>> output = permutations.permuteHeapsAlgorithm(nums);
        assertTrue(output.size() == testResult.size()
                && output.containsAll(testResult)
                && testResult.containsAll(output));
    }

    /**
     * The sixth test for Permutations.
     */
    public void testPermutations6() {
        int[] nums = {1};
        List<List<Integer>> testResult = new ArrayList<>();
        testResult.add(Arrays.asList(new Integer[] {1}));
        Permutations permutations = new Permutations();
        List<List<Integer>> output = permutations.permuteHeapsAlgorithm(nums);
        assertTrue(output.size() == testResult.size()
                && output.containsAll(testResult)
                && testResult.containsAll(output));
    }
}
