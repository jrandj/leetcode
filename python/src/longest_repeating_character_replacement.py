class Solution:
    """
    You are given a string s and an integer k. You can choose any character of the string and change it to any other
    uppercase English character. You can perform this operation at most k times.

    Return the length of the longest substring containing the same letter you can get after performing the above
    operations.
    """

    def characterReplacement(self, s: str, k: int) -> int:
        """
        Return the length of the longest substring containing the same letter you can get after performing the above
        operations.

        :param s: The input string.
        :type s: Str.
        :param k: The number of characters you can replace.
        :type k: Int.
        :return: The length of the longest substring.
        :rtype: Int.

        The time complexity is O(N) where N is the length of s. Faster than 75.67% of solutions.

        The space complexity is O(N) where N is the length of s. Less memory than 56.46% of solutions.
        """
        l, r = 0, 0
        maxf = 0
        res = 0
        count = {}

        while r < len(s):
            # Keep track of characters and their occurrences
            count[s[r]] = 1 + count.get(s[r], 0)
            # Keep track of the most popular element
            maxf = max(maxf, count[s[r]])

            # If we exceed the limit, shrink the left limit
            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            # Keep track of the longest substring.
            res = max(res, r - l + 1)
            r += 1

        return res
