package leetcode;

/**
 * You are climbing a staircase. It takes n steps to reach the top.
 *
 * Each time you can either climb 1 or 2 steps. In how many distinct ways can
 * you climb to the top?
 */
public class ClimbingStairs {

    /**
     * Find the number of distinct ways to climb n steps.
     *
     * @param n The number of stairs.
     * @return The number of distinct ways to climb the steps.
     */
    public int climbStairs(final int n) {

        if (n < 1 || n > 45) {
            return 0;
        }

        int[] result = new int[n];

        if (n == 1) {
            return 1;
        } else if (n == 2) {
            return 2;
        } else {
            result[0] = 1;
            result[1] = 2;
            for (int i = 2; i < n; i++) {
                result[i] = result[i - 1] + result[i - 2];
            }

            return result[n - 1];
        }
    }

}
