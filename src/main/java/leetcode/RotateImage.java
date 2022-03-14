package leetcode;

/**
 * You are given an n x n 2D matrix representing an image, rotate the image by
 * 90 degrees (clockwise).
 *
 * You have to rotate the image in-place, which means you have to modify the
 * input 2D matrix directly. DO NOT allocate another 2D matrix and do the
 * rotation.
 */
public class RotateImage {
    /**
     * Rotate a matrix by 90 degrees clockwise.
     *
     * The time complexity is O(N) as you iterate through each element.
     *
     * The space complexity is constant as no new data structure is created.
     *
     * @param matrix the matrix to rotate
     */
    public void rotate(final int[][] matrix) {
        int size = matrix.length;

        if (size < 1 || size > 20) {
            return;
        }

        // transpose the matrix
        for (int i = 0; i < size; i++) {
            for (int j = i; j < size; j++) {

                if (matrix[i][j] < -1000 || matrix[i][j] > 1000) {
                    return;
                }

                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }

        // flip the matrix horizontally
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < (size / 2); j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[i][size - 1 - j];
                matrix[i][size - 1 - j] = temp;
            }
        }
    }
}
