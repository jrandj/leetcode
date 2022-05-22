package leetcode;

import org.junit.Assert;
import junit.framework.TestCase;

public class FindFirstAndLastPositionOfElementInSortedArrayTest
        extends TestCase {

    /**
     * The first test for FindFirstAndLastPositionOfElementInSortedArray.
     */
    @SuppressWarnings("checkstyle:LineLength")
    public void testFindFirstAndLastPositionOfElementInSortedArray1() {
        int[] testResult = {3, 4};
        int[] nums = {5, 7, 7, 8, 8, 10};
        int target = 8;
        FindFirstAndLastPositionOfElementInSortedArrray findFirstAndLastPositionOfElementInSortedArrray = new leetcode.FindFirstAndLastPositionOfElementInSortedArrray();
        int[] output = findFirstAndLastPositionOfElementInSortedArrray
                .searchRange(nums, target);
        Assert.assertArrayEquals(testResult, output);
    }

    /**
     * The second test for FindFirstAndLastPositionOfElementInSortedArray.
     */
    @SuppressWarnings("checkstyle:LineLength")
    public void testFindFirstAndLastPositionOfElementInSortedArray2() {
        int[] testResult = {-1, -1};
        int[] nums = {5, 7, 7, 8, 8, 10};
        int target = 6;
        FindFirstAndLastPositionOfElementInSortedArrray findFirstAndLastPositionOfElementInSortedArrray = new leetcode.FindFirstAndLastPositionOfElementInSortedArrray();
        int[] output = findFirstAndLastPositionOfElementInSortedArrray
                .searchRange(nums, target);
        Assert.assertArrayEquals(testResult, output);
    }

    /**
     * The third test for FindFirstAndLastPositionOfElementInSortedArray.
     */
    @SuppressWarnings("checkstyle:LineLength")
    public void testFindFirstAndLastPositionOfElementInSortedArray3() {
        int[] testResult = {-1, -1};
        int[] nums = {};
        int target = 0;
        FindFirstAndLastPositionOfElementInSortedArrray findFirstAndLastPositionOfElementInSortedArrray = new leetcode.FindFirstAndLastPositionOfElementInSortedArrray();
        int[] output = findFirstAndLastPositionOfElementInSortedArrray
                .searchRange(nums, target);
        Assert.assertArrayEquals(testResult, output);
    }

}
