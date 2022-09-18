from typing import List


class Solution:
    """
    Write an efficient algorithm that searches for a value target in an m x n integer matrix. This matrix has the
    following properties:
        - Integers in each row are sorted from left to right.
        - The first integer of each row is greater than the last integer of the previous row.
    """

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Searches for a value target in an m x n integer matrix.

        :param matrix: The m x n integer matrix with each row sorted.
        :type matrix: List[List[int]]
        :param target: The number to find in the matrix.
        :type target: Int.
        :return: True if the value is in the matrix, and False if it is not in the matrix.
        :rtype: Bool.

        The time complexity is O(LOG(M*N)) for the binary search. Faster than 10.97% of solutions.

        The space complexity is O(1) as we don't use any additional data structures. Less memory thatn 43.26% of
        solutions.
        """
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, rows * cols

        while l < r:
            m = l + (r - l) // 2
            # matrix[row][column]
            # m // cols gives you the row number, and m % cols gives you how far past that row you are
            m_val = matrix[m // cols][m % cols]
            if m_val > target:
                r = m
            elif m_val < target:
                l = m + 1
            else:
                return True

        return False
