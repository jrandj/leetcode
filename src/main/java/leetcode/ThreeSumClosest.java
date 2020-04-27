package leetcode;

import java.util.Arrays;

/**
 * Given an array nums of n integers and an integer target, find three integers
 * in nums such that the sum is closest to target. Return the sum of the three
 * integers. You may assume that each input would have exactly one solution.
 * 
 * Example:
 * 
 * Given array nums = [-1, 2, 1, -4], and target = 1.
 * 
 * The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
 */
class ThreeSumClosest {
	/**
	 * Return the sum closest to the target.
	 *
	 * @param nums   the array of ints
	 * @param target the target sum
	 * @return the sum of the closest 3 ints
	 */
	public static int threeSumClosest(int[] nums, int target) {
		int currentDifference;
		int previousDifference;
		previousDifference = Integer.MAX_VALUE;

		int returnValue = 0;
		Arrays.sort(nums);
		for (int i = 0; i < nums.length - 2; i++) {
			// low and high are the bounds for the subsequent 2 numbers
			int low = i + 1;
			int high = nums.length - 1;
			while (low < high) {
				currentDifference = Math.abs(nums[i] + nums[low] + nums[high] - target); // minimise this value
				if (currentDifference < previousDifference) { // getting closer to target
					previousDifference = currentDifference;
					returnValue = nums[i] + nums[low] + nums[high];
				}

				// need smaller number, exclude the largest number
				if (nums[i] + nums[low] + nums[high] > target) {
					high--;
				// need larger number, exclude the smallest number
				} else {
					low++;
				}
			}
		}
		return returnValue;
	}
}