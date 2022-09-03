class Solution:
    """
    A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
    non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters
    and numbers.

    Given a string s, return true if it is a palindrome, or false otherwise.
    """

    def isPalindrome(self, s: str) -> bool:
        """
        Given a string s, return true if it is a palindrome, or false otherwise.

        :param s: The input string.
        :type s: Str.
        :return: True if s is a palindrome, and False otherwise.
        :rtype: Bool.

        The time complexity is O(N) as it iterates through the input once. Faster than 81.74% of solutions.

        The space complexity is O(1) as no additional data structures are used. Less memory than 85.73% of solutions.
        """
        l, r = 0, len(s) - 1

        # handle input edge cases
        if len(s) == 1:
            return True
        elif len(s) > int(2e5) or len(s) == 0:
            return False

        while l < r:
            left_char, right_char = s[l].lower(), s[r].lower()

            # skip over non-alpha-numeric characters
            while not left_char.isalnum() and l < r:
                l += 1
                left_char = s[l].lower()
            while not right_char.isalnum() and l < r:
                r -= 1
                right_char = s[r].lower()

            # check if we have a palindrome so far
            if left_char == right_char:
                l += 1
                r -= 1
            else:
                return False

        return True
