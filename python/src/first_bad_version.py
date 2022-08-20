# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    """
    You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version
    of your product fails the quality check. Since each version is developed based on the previous version, all the
    versions after a bad version are also bad.

    Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the
    following ones to be bad.

    You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find
    the first bad version. You should minimize the number of calls to the API.
    """

    def firstBadVersion(self, n: int) -> int:
        """
        Implement a function to find the first bad version. You should minimize the number of calls to the API.

        :param n: The int representing the version.
        :return int: The int representing the first bad version.

        The time complexity is O(N LOG(N)) as we halve the search space every iteration. Faster than 60.54% of
        solutions.

        The space complexity is O(1) as we don't use any additional data structures. Less memory than 97.06% of
        solutions.
        """
        left, right = 0, n

        while left <= right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                # reduce the search space after mid
                right = mid - 1
            else:
                # reduce the search space before mid
                left = mid + 1

        return left
