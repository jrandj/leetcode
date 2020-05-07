package leetcode;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Map;
import java.util.Set;

/**
 * Given a string containing just the characters '(', ')', '{', '}', '[' and
 * ']', determine if the input string is valid.
 * 
 * An input string is valid if:
 * 
 * Open brackets must be closed by the same type of brackets. Open brackets must
 * be closed in the correct order. Note that an empty string is also considered
 * valid.
 */
class ValidParentheses {
	/**
	 * Return whether a String contains valid parenthesis.
	 *
	 * @param s the input String
	 * @return if the input String is a valid input string
	 */
	public static boolean isValid(String s) {

		int leftPointer = 0;
		int rightPointer = 0;

		if (s.length() % 2 == 0) {
			leftPointer = s.length() / 2 - 1;
			rightPointer = s.length() / 2;
		} else {
			return false;
		}

		while (isSubStringValid(s, leftPointer, rightPointer)) {
			if (rightPointer == s.length() - 1 && leftPointer == 0) {
				return true;
			}
			rightPointer += 1;
			leftPointer -= 1;

		}

		return false;

	}

	public static boolean isSubStringValid(String s, int leftPointer, int rightPointer) {

		if (s.charAt(leftPointer) == '{' && s.charAt(leftPointer) == '}') {
			return true;
		} else if (s.charAt(leftPointer) == '(' && s.charAt(rightPointer) == ')') {
			return true;
		} else if (s.charAt(leftPointer) == '[' && s.charAt(rightPointer) == ']') {
			return true;
		}
		return false;
	}
}
