package leetcode;

/**
 * Given a string s, find the longest palindromic substring in s. You may assume
 * that the maximum length of s is 1000.
 */
public final class LongestPalindrome {

    private LongestPalindrome() {
        // prevent instantiation
    }

    /**
     * The brute force solution. Find every substring and find the longest where
     * it equals its reverse.
     *
     * @param s the input String
     * @return the reversed string
     */
    public static String reverseString(final String s) {
        StringBuilder reverseString = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            reverseString = reverseString
                    .append((s.charAt(s.length() - i - 1)));
        }
        return reverseString.toString();
    }

    /**
     * The brute force solution.
     *
     * @param s the input String
     * @return the reversed string
     */
    public static String longestPalindromeSolution1(final String s) {
        StringBuilder longestPalindrome = new StringBuilder();
        StringBuilder longestCandidate = new StringBuilder();

        if (s == null || s.equals("")) {
            return "";
        }

        for (int i = 0; i < s.length(); i++) {
            for (int j = i; j < s.length(); j++) {
                longestCandidate.append(s.charAt(j));
                String reverseStringCandidate = reverseString(
                        longestCandidate.toString());
                if (longestCandidate.toString().equals(reverseStringCandidate)
                        && (longestCandidate.length() > longestPalindrome
                                .length())) {
                    longestPalindrome = longestCandidate;
                }
            }
        }
        return longestPalindrome.toString();
    }

    /**
     * Expand around centre.
     *
     * @param s           the input String
     * @param pstartIndex the starting index for expansion
     * @param pendIndex   the ending index for expansion
     * @return the expanded substring
     */
    public static String expand(final String s, final int pstartIndex,
            final int pendIndex) {
        int startIndex = pstartIndex;
        int endIndex = pendIndex;
        while (startIndex >= 0 && endIndex < s.length()) {
            if (s.charAt(startIndex) == s.charAt(endIndex)) {
                startIndex--;
                endIndex++;
            } else {
                break;
            }
        }
        // 1 has been subtracted from startIndex and endIndex, so we need to add
        // 1 back when we return
        // (noting that the substring method goes from start to end - 1)
        return s.substring(startIndex + 1, endIndex);
    }

    /**
     * Expand around the centre for both i:i and i:i+1.
     *
     * @param s the input String
     * @return the longest palindrome
     */
    public static String longestPalindromeSolution2(final String s) {
        int stringLength = s.length();
        String longestPalindrome = "";
        String longestCandidate1 = "";
        String longestCandidate2 = "";

        for (int i = 0; i < stringLength; i++) {
            // E.g. "ACA" gets picked up in the first statement and "ACCA" gets
            // picked up in the second
            // every palindrome is one of these patterns
            longestCandidate1 = expand(s, i, i);
            if (longestCandidate1.length() > longestPalindrome.length()) {
                longestPalindrome = longestCandidate1;
            }
            longestCandidate2 = expand(s, i, i + 1);
            if (longestCandidate2.length() > longestPalindrome.length()) {
                longestPalindrome = longestCandidate2;
            }
        }
        return longestPalindrome;
    }
}
