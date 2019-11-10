package leetcode;

import java.util.Arrays;

/**
 * The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
 * (you may want to display this pattern in a fixed font for better legibility)
 * 
 *   P   A   H   N
 *   A P L S I I G
 *   Y   I   R
 *   
 * And then read line by line: "PAHNAPLSIIGYIR"
 * 
 * Write the code that will take a string and make this conversion given a number of rows.
 */
public class zigZagConversion {

  public static String convert(String s, int numRows) {
    Character[][] matrix = new Character[numRows][s.length()];
    int i = 0;
    int j = 0;
    int index = 0;
    int dir = 1;
    int length = s.length();
    String output = "";

    if (s == null || s.isEmpty()) {
      return "";
    }

    if (numRows == 1) {
      return s;
    }

    // build matrix
    while (index < length) {
      matrix[i][j] = s.charAt(index);
      index++;

      // boundary condition
      if (i == numRows - 1 && dir == 1) {
        dir = -1;
      }

      // boundary condition
      if (i == 0 && dir == -1) {
        dir = 1;
      }

      if (dir == -1) {
        j++;
      }

      i = i + dir;
    }

    // print matrix
    for (int x = 0; x < numRows; x++) {
      for (int y = 0; y < length; y++) {
        if (matrix[x][y] != null) {
          output += matrix[x][y];
        }
      }
    }

    return output;
  }
}
