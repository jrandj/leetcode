package leetcode;

/**
 * Given a string s, find the longest palindromic substring in s. You may assume that the maximum
 * length of s is 1000.
 */
public class LongestPalindrome {
  /**
   * The brute force solution. Find every substring and find the longest where it equals its
   * reverse.
   */
  public static String reverseString(String s) {
    String reverseString = new String();
    for (int i = 0; i < s.length(); i++) {
      reverseString = reverseString + (s.charAt(s.length() - i - 1));
    }
    return reverseString;
  }

  /**
   * The brute force solution.
   */
  public static String longestPalindromeSolution1(String s) {
    String longestPalindrome = "";
    String longestCandidate = new String();

    if (s.equals("") || s == null) {
      return "";
    }

    for (int i = 0; i < s.length(); i++) {
      longestCandidate = "";
      for (int j = i; j < s.length(); j++) {
        longestCandidate = longestCandidate + s.charAt(j);
        String reverseStringCandidate = reverseString(longestCandidate);
        if (longestCandidate.equals(reverseStringCandidate)
            && (longestCandidate.length() > longestPalindrome.length())) {
          longestPalindrome = longestCandidate;
        }
      }
    }
    return longestPalindrome;
  }

  /**
   * Expand around centre.
   */
  public static String expand(String s, int startIndex, int endIndex) {
    while (startIndex >= 0 && endIndex < s.length()) {
      if (s.charAt(startIndex) == s.charAt(endIndex)) {
        startIndex--;
        endIndex++;
      } else {
        break;
      }
    }
    // 1 has been subtracted from startIndex and endIndex, so we need to add 1 back when we return
    // (noting that the substring method goes from start to end - 1)
    return s.substring(startIndex + 1, endIndex);
  }

  /**
   * Expand around the centre for both i:i and i:i+1.
   */
  public static String longestPalindromeSolution2(String s) {
    int stringLength = s.length();
    String longestPalindrome = "";
    String longestCandidate1 = "";
    String longestCandidate2 = "";

    for (int i = 0; i < stringLength; i++) {
      // E.g. "ACA" gets picked up in the first statement and "ACCA" gets picked up in the second
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
