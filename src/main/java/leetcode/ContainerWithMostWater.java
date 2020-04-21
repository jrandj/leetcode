package leetcode;

/**
 * Given n non-negative integers a1, a2, ..., an , where each represents a point
 * at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
 * of line i is at (i, ai) and (i, 0). Find two lines, which together with
 * x-axis forms a container, such that the container contains the most water.
 * 
 * Note: You may not slant the container and n is at least 2.
 *
 */
class ContainerWithMostWater {
	/**
	 * Return maximum area.
	 *
	 * @param height an array of coordinates
	 * @return maximum area
	 */
	public static int maxArea(int[] height) {
		int maxArea = 0;
		int area = 0;
		for (int i = 0; i < height.length; i++) {
			for (int j = i; j < height.length; j++) {
				if (height[i] > height[j]) {
					area = height[j] * Math.abs(i - j);
				} else {
					area = height[i] * Math.abs(i - j);
				}

				if (area > maxArea) {
					maxArea = area;
				}
			}
		}
		return maxArea;
	}

}