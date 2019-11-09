package leetcode;

import java.util.Arrays;
import junit.framework.TestCase;

public class zigZagConversionTest extends TestCase {
  public void testzigZagConversion1() {
    int numRows = 3;
    String result = "PAHNAPLSIIGYIR";
    String inputString = "PAYPALISHIRING";
    String outputString;
    outputString = leetcode.zigZagConversion.convert(inputString, numRows);
    assertEquals(outputString, result);
  }

  public void testzigZagConversion2() {
    int numRows = 4;
    String result = "PINALSIGYAHRPI";
    String inputString = "PAYPALISHIRING";
    String outputString;
    outputString = leetcode.zigZagConversion.convert(inputString, numRows);
    assertEquals(outputString, result);
  }
  
  public void testzigZagConversion3() {
    int numRows = 1;
    String result = "AB";
    String inputString = "AB";
    String outputString;
    outputString = leetcode.zigZagConversion.convert(inputString, numRows);
    assertEquals(outputString, result);
  }
}
