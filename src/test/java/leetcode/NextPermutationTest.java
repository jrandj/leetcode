package leetcode;

import org.junit.Assert;
import junit.framework.TestCase;

public class NextPermutationTest extends TestCase {

    /**
     * The first test for NextPermutation.
     */
    public void testNextPermutation1() {
        NextPermutation nextPermutation = new NextPermutation();
        int[] nums = {1, 2, 3};
        int[] testResult = {1, 3, 2};
        nextPermutation.nextPermutation(nums);
        Assert.assertArrayEquals(nums, testResult);
    }

    /**
     * The second test for NextPermutation.
     */
    public void testNextPermutation2() {
        NextPermutation nextPermutation = new NextPermutation();
        int[] nums = {3, 2, 1};
        int[] testResult = {1, 2, 3};
        nextPermutation.nextPermutation(nums);
        Assert.assertArrayEquals(nums, testResult);
    }

    /**
     * The third test for NextPermutation.
     */
    public void testNextPermutation3() {
        NextPermutation nextPermutation = new NextPermutation();
        int[] nums = {1, 1, 5};
        int[] testResult = {1, 5, 1};
        nextPermutation.nextPermutation(nums);
        Assert.assertArrayEquals(nums, testResult);
    }

    /**
     * The fourth test for NextPermutation.
     */
    public void testNextPermutation4() {
        NextPermutation nextPermutation = new NextPermutation();
        int[] nums = {1, 3, 2};
        int[] testResult = {2, 1, 3};
        nextPermutation.nextPermutation(nums);
        Assert.assertArrayEquals(nums, testResult);
    }

    /**
     * The fifth test for NextPermutation.
     */
    public void testNextPermutation5() {
        NextPermutation nextPermutation = new NextPermutation();
        int[] nums = {1};
        int[] testResult = {1};
        nextPermutation.nextPermutation(nums);
        Assert.assertArrayEquals(nums, testResult);
    }

}
