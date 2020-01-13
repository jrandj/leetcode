package leetcode;

import java.util.Arrays;
import junit.framework.TestCase;

public class TwoSumTest extends TestCase {
  public void testtwoSumExpectedResult1() {
    int[] result;
    int[] nums = {2, 7, 11, 15};
    int target = 9;
    int[] testResult = {0, 1};

    result = leetcode.TwoSum.twoSumSolution(nums, target);
    assertEquals(Arrays.toString(testResult), Arrays.toString(result));
  }

  public void testtwoSumExpectedResult2() {
    int[] result;
    int[] nums = {3, 2, 3};
    int target = 6;
    int[] testResult = {0, 2};

    result = leetcode.TwoSum.twoSumSolution(nums, target);
    assertEquals(Arrays.toString(testResult), Arrays.toString(result));
  }


  public void testtwoSumExpectedResult3() {
    int[] result;
    int[] nums = {2, 5, 5, 11};
    int target = 10;
    int[] testResult = {1, 2};

    result = leetcode.TwoSum.twoSumSolution(nums, target);
    assertEquals(Arrays.toString(testResult), Arrays.toString(result));
  }
}
