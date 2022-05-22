package leetcode;

import junit.framework.TestCase;

public class SearchInRotatedSortedArrayTest extends TestCase {

    /**
     * The first test for SearchInRotatedSortedArray.
     */
    public void testSearchInRotatedSortedArray1() {
        int testResult = 4;
        int[] nums = {4, 5, 6, 7, 0, 1, 2};
        int target = 0;
        SearchInRotatedSortedArray searchInRotatedSortedArray =
                new leetcode.SearchInRotatedSortedArray();
        int output = searchInRotatedSortedArray.searchNaive(nums, target);
        assertEquals(testResult, output);
    }

    /**
     * The second test for SearchInRotatedSortedArray.
     */
    public void testSearchInRotatedSortedArray2() {
        int testResult = -1;
        int[] nums = {4, 5, 6, 7, 0, 1, 2};
        int target = 3;
        SearchInRotatedSortedArray searchInRotatedSortedArray =
                new leetcode.SearchInRotatedSortedArray();
        int output = searchInRotatedSortedArray.searchNaive(nums, target);
        assertEquals(testResult, output);
    }

    /**
     * The third test for SearchInRotatedSortedArray.
     */
    public void testSearchInRotatedSortedArra3() {
        int testResult = -1;
        int[] nums = {1};
        int target = 0;
        SearchInRotatedSortedArray searchInRotatedSortedArray =
                new leetcode.SearchInRotatedSortedArray();
        int output = searchInRotatedSortedArray.searchNaive(nums, target);
        assertEquals(testResult, output);
    }

    /**
     * The first test for SearchInRotatedSortedArray.
     */
    public void testSearchInRotatedSortedArray4() {
        int testResult = 4;
        int[] nums = {4, 5, 6, 7, 0, 1, 2};
        int target = 0;
        SearchInRotatedSortedArray searchInRotatedSortedArray =
                new leetcode.SearchInRotatedSortedArray();
        int output = searchInRotatedSortedArray.searchMergeSort(nums, target);
        assertEquals(testResult, output);
    }

    /**
     * The second test for SearchInRotatedSortedArray.
     */
    public void testSearchInRotatedSortedArray5() {
        int testResult = -1;
        int[] nums = {4, 5, 6, 7, 0, 1, 2};
        int target = 3;
        SearchInRotatedSortedArray searchInRotatedSortedArray =
                new leetcode.SearchInRotatedSortedArray();
        int output = searchInRotatedSortedArray.searchMergeSort(nums, target);
        assertEquals(testResult, output);
    }

    /**
     * The third test for SearchInRotatedSortedArray.
     */
    public void testSearchInRotatedSortedArra6() {
        int testResult = -1;
        int[] nums = {1};
        int target = 0;
        SearchInRotatedSortedArray searchInRotatedSortedArray =
                new leetcode.SearchInRotatedSortedArray();
        int output = searchInRotatedSortedArray.searchMergeSort(nums, target);
        assertEquals(testResult, output);
    }

}
