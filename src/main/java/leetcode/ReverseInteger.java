package leetcode;

/**
 * Given a 32-bit signed integer, reverse digits of an integer. Note: Assume we are dealing with an
 * environment which could only store integers within the 32-bit signed integer range: [−231, 231 −
 * 1]. For the purpose of this problem, assume that your function returns 0 when the reversed
 * integer overflows.
 */
public class ReverseInteger {
  public static int reverse(int x) {
    String myString = Integer.toString(x);
    String myStringReversed = "";
    int result;
    boolean firstNonZero = false;

    for (int i = myString.length() - 1; i >= 0; i--) {
      if (i == 0 && x < 0) {
        break;
      }

      if (myString.charAt(i) != '0') {
        firstNonZero = true;
      }

      if (firstNonZero) {
        myStringReversed += myString.charAt(i);
      }
    }

    if (x < 0) {
      myStringReversed = "-" + myStringReversed;
    }

    try {
      result = Integer.parseInt(myStringReversed);
    } catch (java.lang.NumberFormatException e) {
      result = 0;
    }

    return (x == 0) ? 0 : result;
  }
}
