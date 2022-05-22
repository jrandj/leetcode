package leetcode;

/**
 * Given an input string (s) and a pattern (p), implement regular expression
 * matching with support for '.' and '*'. '.' Matches any single character. '*'
 * Matches zero or more of the preceding element. The matching should cover the
 * entire input string (not partial).
 */
public final class RegularExpressionMatching {

    private RegularExpressionMatching() {
        // prevent instantiation
    }

    /**
     * Determine whether an integer is a palindrome using a naive approach.
     *
     * @param s the string
     * @param p the pattern
     * @return true if the pattern is in the string and false otherwise
     */
    public static boolean isMatch(final String s, final String p) {
        if (p.length() == 0) {
            return s.length() == 0;
        }

        boolean firstMatch = (s.length() > 0
                && (s.charAt(0) == p.charAt(0) || p.charAt(0) == '.'));

        if (p.length() >= 2 && p.charAt(1) == '*') {
            /*
             * If p[1] = '*' either a) p[0] != s[0] or b) [0] == s[0] If a) can
             * ignore p[0] and p[1] If b) can check rest of s
             */
            return isMatch(s, p.substring(2))
                    || (firstMatch && isMatch(s.substring(1), p));
        } else {
            return firstMatch && isMatch(s.substring(1), p.substring(1));
        }
    }
}
