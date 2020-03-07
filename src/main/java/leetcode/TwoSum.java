package leetcode;

/**
 * Given an array of integers, return indices of the two numbers such that they add up to a specific
 * target. You may assume that each input would have exactly one solution, and you may not use the
 * same element twice.
 */
public class TwoSum {

  public static int[] twoSumSolution(int[] nums, int target) {
    for (int i = 0; i < (nums.length); i++) {
      for (int j = 0; j < (nums.length); j++) {
        if (nums[i] + nums[j] == target) {
          if (i != j) {
            return new int[] {i, j};
          }
        }
      }
    }
    return null;
  }
}
