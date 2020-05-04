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

		// Choice: Place "(" or ")"
		// Constraints: Can't close more parenthesis than we open
		// Goal: Place a string of length n*2

		List<String> result = new LinkedList<>();
		result.add(recursiveHelper(n, n));
		return result;
	}

	private static String recursiveHelper(int l, int r) {
		String ch = "";
		while (l > 0) {
			if (l == r) {
				// lol this will always be called
				recursiveHelper(l - 1, r - 1);
				l -= 1;
				r -= 1;
			} else if (r > l) {
				recursiveHelper(l, r - 1);
				r -= 1;
			} else {
				recursiveHelper(l - 1, r);
				l -= 1;
			}
		}
		
		if (l > r) {
			ch += "(";
		} else if (r > l) {
			ch += ")";
		} else {
			ch += "()";
		}
		String result = ch.toString();
		return result;
	}
}