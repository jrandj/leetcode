package leetcode;

/**
 * Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same
 * backward as forward.
 */
public class PalindromeNumber {

  public static boolean isPalindrome2(int x) {
    // if x is only one digit it is a palindrom
    // if x is negative it is not a palindrome
    if (x == 0) {
      return true;
    }

    if (x < 0 || x % 10 == 0) {
      return false;
    }

    int reversedInt = 0;
    // System.out.println("x: " + x);
    while (x > reversedInt) {
      // get the last digit of x
      int pop = x % 10;
      System.out.println("pop: " + pop);
      // look at the previous digit
      x = x / 10;
      // System.out.println("x: " + x);
      reversedInt = (reversedInt * 10) + pop;
      // System.out.println("reversedInt: " + reversedInt);
    }

    if (x == reversedInt || x == reversedInt / 10) {
      return true;
    } else {
      return false;
    }
  }

  public static boolean isPalindrome1(int x) {

    String intString = Integer.toString(x);
    String reverseString = "";

    for (int i = intString.length() - 1; i >= 0; i--) {
      if (intString.charAt(i) == '+' || intString.charAt(i) == '-') {
        break;
      }
      reverseString += intString.charAt(i);
    }

    System.out.println("intString: " + intString + " " + " reverseString: " + reverseString);

    if (intString.equals(reverseString)) {
      return true;
    } else {
      return false;
    }
  }
}
