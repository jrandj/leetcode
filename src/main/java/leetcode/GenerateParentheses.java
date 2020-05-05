package leetcode;

import java.util.LinkedList;
import java.util.List;

/**
 * Given n pairs of parentheses, write a function to generate all combinations
 * of well-formed parentheses.
 * 
 * For example, given n = 3, a solution set is:
 * 
 * [ "((()))", "(()())", "(())()", "()(())", "()()()" ]
 */
class GenerateParentheses {
	/**
	 * Return all all combinations of well-formed parentheses.
	 *
	 * @param n the number of pairs of parentheses
	 * @return the List<String> of all well-formed parentheses
	 */
	public static List<String> generateParenthesis(int n) {
		List<String> result = new LinkedList<>();
		String candidate = new String();
		recursiveHelper(candidate, n, result);
		return result;
	}

	private static void recursiveHelper(String candidate, int n, List<String> result) {
		if (candidate.length() == 2 * n) {
			result.add(candidate); // Goal: Place a string of length n*2
		} else {
			int leftCount = 0;
			int rightCount = 0;
			for(int i = 0; i < candidate.length(); i++) {
				if(candidate.charAt(i) == '(') {
					leftCount++;
				}
				if(candidate.charAt(i) == ')') {
					rightCount++;
				}
			}
			// Choice: Place "(" or ")"
			// Constraints: Can't close more parenthesis than we open
			if (leftCount == rightCount) { // Can open more if we have the same number (haven't hit 2*N)
				recursiveHelper(candidate + "(", n, result);
			} else if (leftCount > rightCount) {
				if (leftCount < n) { // Can open more if we haven't hit length yet
					recursiveHelper(candidate + "(", n, result);
				}
				recursiveHelper(candidate + ")", n, result); // Need to close
			}
		}
	}
}