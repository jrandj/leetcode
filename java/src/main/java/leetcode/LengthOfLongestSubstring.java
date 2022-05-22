package leetcode;

import java.util.HashSet;
import java.util.Set;

/**
 * Given a string, find the length of the longest substring without repeating
 * characters.
 */
public final class LengthOfLongestSubstring {

    private LengthOfLongestSubstring() {
        // prevent instantiation
    }

    /**
     * Finds the length of the longest substring without repeating character.
     *
     * @param s The input string
     * @return longest The longest substring without repeating characters
     */
    public static int lengthOfLongestSubstringSolution(final String s) {
        int longest = 0;
        int length;

        // For each character in the string
        for (int i = 0; i < s.length(); i++) {
            // Each character is a candidate for start of longest substring
            Set<Character> candidate = new HashSet<Character>();
            // For each substring starting at the i'th character
            for (int j = i; j < s.length(); j++) {
                // Add j'th character if it's not in the set
                if (candidate.contains(s.charAt(j))) {
                    break;
                }
                candidate.add(s.charAt(j));
            }

            // Get the length and set it as the longest if it is the longest
            length = candidate.size();
            if (length > longest) {
                longest = length;
            }
        }
        // Handle edge cases
        longest = (s.length() == 0) ? 0 : longest;
        longest = (s.length() == 1) ? 1 : longest;
        return longest;
    }

}
