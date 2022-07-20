class Solution:
    """
    Given a string s, return the longest palindromic substring in s.
    """

    def longestPalindrome(self, s: str) -> str:
        """
        Given a string s, return the longest palindromic substring in s.

        :param s: The input string.
        :return str: The longest palindromic substring in s.

        The time complexity is O(N^2) as for each element we find the longest palindrome. Faster than 56.95% of
        solutions.

        The space complexity is O(1) as only constants are used. Less memory than 91.28% of solutions.
        """
        max_length_l, max_length_r = 0, 0

        for i in range(len(s)):
            odd_l, odd_r = self.expand_around_centre(s, i, i)
            even_l, even_r = self.expand_around_centre(s, i, i + 1)

            if even_r - even_l > max_length_r - max_length_l:
                max_length_r, max_length_l = even_r, even_l

            if odd_r - odd_l > max_length_r - max_length_l:
                max_length_r, max_length_l = odd_r, odd_l

        max_length_palindrome = s[max_length_l:max_length_r]
        return max_length_palindrome

    @staticmethod
    def expand_around_centre(s: str, l: int, r: int) -> tuple:
        """
        A helper function to find palindromes.

        :param s: The input string.
        :param l: The starting index for the left.
        :param r: The starting index for the right.
        :return tuple: The left and right indices of the palindrome.
        """
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1

        return l + 1, r
