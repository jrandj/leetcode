package leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Given an array nums of n integers, are there elements a, b, c in nums such
 * that a + b + c = 0? Find all unique triplets in the array which gives the sum
 * of zero.
 * 
 * Note: The solution set must not contain duplicate triplets. Example:
 * 
 * Given array nums = [-1, 0, 1, 2, -1, -4],
 * 
 * A solution set is: [ [-1, 0, 1], [-1, -1, 2] ]
 */
class ThreeSum {
	/**
	 * Return unique triplets that sum to zero.
	 *
	 * @param nums the array of ints
	 * @return a list of lists that satisfy the criteria
	 */

	public static List<List<Integer>> threeSum(int[] nums) {
		// sort the list as the bounds search requires it
		Arrays.sort(nums);
		List<List<Integer>> outputArray = new ArrayList<List<Integer>>();
		// for each number, look for 2 subsequent numbers that give a total sum of 0
		for (int i = 0; i < nums.length - 2; i++) {
			if (nums[i] > 0) {
				break;
			}
			// if a number is the same as the previous number skip it
			if (i == 0 || nums[i] != nums[i - 1]) {
				// low and high are the bounds for the subsequent 2 numbers
				int low = i + 1;
				int high = nums.length - 1;
				int sum = 0 - nums[i];
				while (low < high) {
					if (nums[low] + nums[high] == sum) {
						outputArray.add(Arrays.asList(nums[i], nums[low], nums[high]));
						// increment search bounds but skip over duplicates first
						// if a number is the same as the previous number skip it
						while (low < high && nums[low] == nums[low + 1]) {
							low++;
						}
						// if a number is the same as the previous number skip it
						while (low < high && nums[high] == nums[high - 1]) {
							high--;
						}
						low++;
						high--;
					} else if (nums[low] + nums[high] > sum) { // increment search bounds
						high--;
					} else
						low++;
				}
			}
		}
		return outputArray;
	}
}