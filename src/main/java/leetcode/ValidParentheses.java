package leetcode;

import java.util.Stack;

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
final class ValidParentheses {

    private ValidParentheses() {
        // prevent instantiation
    }

    /**
     * Return whether a String contains valid parenthesis.
     *
     * @param s the input String
     * @return if the input String is a valid input string
     */
    public static boolean isValid(final String s) {
        Stack<Character> myStack = new Stack<>();

        for (int i = 0; i < s.length(); i++) {

            char ch = s.charAt(i);
            if (ch == '(' || ch == '[' || ch == '{') {
                myStack.add(ch);
            } else if (ch == ')' || ch == ']' || ch == '}') {
                if (myStack.isEmpty()) {
                    return false;
                }
                switch (ch) {
                case ')':
                    if (myStack.peek() != '(') {
                        return false;
                    }
                    break;
                case ']':
                    if (myStack.peek() != '[') {
                        return false;
                    }
                    break;
                case '}':
                    if (myStack.peek() != '{') {
                        return false;
                    }
                    break;
                default:
                }
                myStack.pop();
            } else {
                return false;
            }
        }
        return myStack.isEmpty();
    }
}
