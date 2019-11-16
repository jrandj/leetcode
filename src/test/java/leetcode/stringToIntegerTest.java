package leetcode;

import junit.framework.TestCase;

public class stringToIntegerTest extends TestCase {
  public void testStringToInteger1() {
    int result = 42;
    String input = "42";
    int output = leetcode.StringToInteger.myAtoi(input);
    assertEquals(output, result);
  }
  
  public void testStringToInteger2() {
    int result = -42;
    String input = "-42";
    int output = leetcode.StringToInteger.myAtoi(input);
    assertEquals(output, result);
  }

  public void testStringToInteger3() {
    int result = 4193;
    String input = "4193 with words";
    int output = leetcode.StringToInteger.myAtoi(input);
    assertEquals(output, result);
  }
  
  public void testStringToInteger4() {
    int result = 0;
    String input = "words and 987";
    int output = leetcode.StringToInteger.myAtoi(input);
    assertEquals(output, result);
  }
  
  public void testStringToInteger5() {
    int result = -2147483648;
    String input = "-91283472332";
    int output = leetcode.StringToInteger.myAtoi(input);
    assertEquals(output, result);
  }
  
  public void testStringToInteger6() {
    int result = 3;
    String input = "3.14159";
    int output = leetcode.StringToInteger.myAtoi(input);
    assertEquals(output, result);
  }
  
  public void testStringToInteger7() {
    int result = 0;
    String input = "-";
    int output = leetcode.StringToInteger.myAtoi(input);
    assertEquals(output, result);
  }
  
  public void testStringToInteger8() {
    int result = 1;
    String input = "+1";
    int output = leetcode.StringToInteger.myAtoi(input);
    assertEquals(output, result);
  }
  
  public void testStringToInteger9() {
    int result = 12345678;
    String input = "  0000000000012345678";
    int output = leetcode.StringToInteger.myAtoi(input);
    assertEquals(output, result);
  }
  
  public void testStringToInteger10() {
    int result = 0;
    String input = "+-2";
    int output = leetcode.StringToInteger.myAtoi(input);
    assertEquals(output, result);
  }
  
  public void testStringToInteger11() {
    int result = 0;
    String input = "0-1";
    int output = leetcode.StringToInteger.myAtoi(input);
    assertEquals(output, result);
  }
  
  public void testStringToInteger12() {
    int result = 123;
    String input = "123-";
    int output = leetcode.StringToInteger.myAtoi(input);
    assertEquals(output, result);
  }

}
