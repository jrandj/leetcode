package leetcode;

import junit.framework.TestCase;

public class ZigZagConversionTest extends TestCase {

    /**
     * The second test for ZigZagConversion.
     */
    public void testzigZagConversion1() {
        int numRows = 3;
        String result = "PAHNAPLSIIGYIR";
        String inputString = "PAYPALISHIRING";
        String outputString;
        outputString = leetcode.ZigZagConversion.convert(inputString, numRows);
        assertEquals(outputString, result);
    }

    /**
     * The second test for ZigZagConversion.
     */
    public void testzigZagConversion2() {
        int numRows = 4;
        String result = "PINALSIGYAHRPI";
        String inputString = "PAYPALISHIRING";
        String outputString;
        outputString = leetcode.ZigZagConversion.convert(inputString, numRows);
        assertEquals(outputString, result);
    }

    /**
     * The third test for ZigZagConversion.
     */
    public void testzigZagConversion3() {
        int numRows = 1;
        String result = "AB";
        String inputString = "AB";
        String outputString;
        outputString = leetcode.ZigZagConversion.convert(inputString, numRows);
        assertEquals(outputString, result);
    }
}
