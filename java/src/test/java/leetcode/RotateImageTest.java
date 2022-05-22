package leetcode;

import junit.framework.TestCase;

public class RotateImageTest extends TestCase {

    /**
     * The first test for Rotate Image.
     */
    public void testRotateImage1() {
        int[][] actualResult = new int[][]{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        int[][] expectedResult = new int[][]{{7, 4, 1}, {8, 5, 2}, {9, 6, 3}};
        RotateImage rotateImage = new RotateImage();
        rotateImage.rotate(actualResult);
        assertTrue(equalsHelper(actualResult, expectedResult));
    }

    /**
     * The second test for Rotate Image.
     */
    public void testRotateImage2() {
        int[][] actualResult = new int[][]{{5, 1, 9, 11}, {2, 4, 8, 10},
                {13, 3, 6, 7}, {15, 14, 12, 16}};
        int[][] expectedResult = new int[][]{{15, 13, 2, 5}, {14, 3, 4, 1},
                {12, 6, 8, 9}, {16, 7, 10, 11}};
                RotateImage rotateImage = new RotateImage();
        rotateImage.rotate(actualResult);
        assertTrue(equalsHelper(actualResult, expectedResult));
    }

    /**
     * Compare two matrices for equality.
     *
     * @param firstMatrix  the first matrix for comparison
     * @param secondMatrix the second matrix for comparison
     * @return true if equal and false otherwise
     */
    public boolean equalsHelper(final int[][] firstMatrix,
            final int[][] secondMatrix) {

        for (int i = 0; i < firstMatrix.length; i++) {
            for (int j = 0; j < firstMatrix.length; j++) {
                if (firstMatrix[i][j] != secondMatrix[i][j]) {
                    return false;
                }
            }
        }
        return true;
    }

}
