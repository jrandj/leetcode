class Solution:
    """
    Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome
    that can be built with those letters.

    Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
    """

    def longestPalindrome(self, s: str) -> int:
        """
        Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome
        that can be built with those letters.

        :param s: The input string.
        :type s: Str.
        :return: The length of the longest palindrome.
        :rtype: Int.

        The time complexity is O(N) as we iterate through the input once. Faster than 55.41% of solutions.

        The space complexity is O(N) as we use a dict of length N. Less memory than 21.98% of solutions.
        """
        # handle trivial scenario
        if len(s) == 1:
            return 1

        result = 0
        odd_count = 0
        char_counts = {}

        # build a dict containing all characters
        for c in s:
            char_counts[c] = char_counts.get(c, 0) + 1

        for v in char_counts.values():
            # even counts can be used entirely
            if v % 2 == 0:
                result += v
            # odd counts we can use 1 less, with an allowance of 1 for the centre of odd length palindrome
            else:
                result += v - 1
                odd_count = 1

        if odd_count:
            result += 1

        return result
