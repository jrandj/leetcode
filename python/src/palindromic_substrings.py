class Solution:
    """
    Given a string s, return the number of palindromic substrings in it.

    A string is a palindrome when it reads the same backward as forward.

    A substring is a contiguous sequence of characters within the string.
    """

    def __init__(self):
        """
        Initialise the solution.
        """
        self.res = 0

    def countSubstrings_1(self, s: str) -> int:
        """
        Given a string s, return the number of palindromic substrings in it.

        :param s: The input string.
        :type s: Str.
        :return: The number of palindromic substrings.
        :rtype: Int.

        This is the brute force solution for the problem.

        The time complexity is O(N^3) due to 2 nested for loops and checking if each substring is a palindrome.
        Exceeds the time limit.

        The space complexity is O(1) as we don't use any additional data structures.
        """
        # substring can start from any position
        for i in range(0, len(s)):
            # substring can continue from the next position to the end
            for j in range(i + 1, len(s) + 1):
                # slicing end index is exclusive, which is why we add 1 to the inner loop
                candidate = s[i:j]
                if self.is_palindrome(candidate):
                    self.res += 1

        return self.res

    def countSubstrings_2(self, s: str) -> int:
        """
        Given a string s, return the number of palindromic substrings in it.

        :param s: The input string.
        :type s: Str.
        :return: The number of palindromic substrings.
        :rtype: Int.

        The time complexity is O(N^2) for 2 nested loops. Faster than 26.45% of solutions.

        The space complexity is O(1) as we don't use any additional data structures.
        """
        for i in range(len(s)):
            self.res += self.count_palindromes(i, i, s) + self.count_palindromes(i, i + 1, s)
        return self.res

    def count_palindromes(self, l: int, r: int, s: str):
        """
        A helper function to find palindromes.

        :param l: The starting left index.
        :type l: Int.
        :param r: The starting right index.
        :type r: Int.
        :param s: The string to find palindromes in.
        :type s: Str.
        :return: The number of palindromic substrings.
        :rtype: Int.
        """
        count = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        return count

    def is_palindrome(self, s: str):
        """
        Check if a string is a palindrome.

        :param s: The string to be checked.
        :type s: Str.
        :return: True if the string is a palindrome, and False otherwise.
        :rtype: Bool.
        """
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
