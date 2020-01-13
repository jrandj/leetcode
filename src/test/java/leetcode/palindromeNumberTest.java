package leetcode;

import junit.framework.TestCase;

public class PalindromeNumberTest extends TestCase {
  public void testPalindromeNumber1() {
    int input = 121;
    Boolean expectedResult = true;
    Boolean actualResult = leetcode.PalindromeNumber.isPalindrome2(input);
    assertEquals(actualResult, expectedResult);
  }

  public void testPalindromeNumber2() {
    int input = -121;
    Boolean expectedResult = false;
    Boolean actualResult = leetcode.PalindromeNumber.isPalindrome2(input);
    assertEquals(actualResult, expectedResult);
  }

  public void testPalindromeNumber3() {
    int input = 10;
    Boolean expectedResult = false;
    Boolean actualResult = leetcode.PalindromeNumber.isPalindrome2(input);
    assertEquals(actualResult, expectedResult);
  }

  public void testPalindromeNumber4() {
    int input = 1;
    Boolean expectedResult = true;
    Boolean actualResult = leetcode.PalindromeNumber.isPalindrome2(input);
    assertEquals(actualResult, expectedResult);
  }

  public void testPalindromeNumber5() {
    int input = 11;
    Boolean expectedResult = true;
    Boolean actualResult = leetcode.PalindromeNumber.isPalindrome2(input);
    assertEquals(actualResult, expectedResult);
  }

  public void testPalindromeNumber6() {
    int input = 123321;
    Boolean expectedResult = true;
    Boolean actualResult = leetcode.PalindromeNumber.isPalindrome2(input);
    assertEquals(actualResult, expectedResult);
  }

}
