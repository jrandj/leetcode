import sys


class Solution:
    """
    Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that
    every character in t (including duplicates) is included in the window. If there is no such substring, return the
    empty string "".

    The testcases will be generated such that the answer is unique.

    A substring is a contiguous sequence of characters within the string.
    """

    def minWindow(self, s: str, t: str) -> str:
        """
        Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that
        every character in t (including duplicates) is included in the window.

        :param s: The first input string.
        :param t: The second input string.
        :return str: The minimum substring of s such that characters in t are included in the window.

        The time complexity is O(s + t) as we iterate through at most s and t. Faster than 63.84% of solutions.

        The space complexity is O(s + t) for the stack. Less memory than 82.83% of solutions.
        """
        # handle the trivial case
        if t == '':
            return ''

        window, t_chars = {}, {}
        for c in t:
            t_chars[c] = t_chars.get(c, 0) + 1

        have, need = 0, len(t_chars)
        res, res_len = [-1, -1], sys.maxsize
        l = 0

        for r in range(len(s)):
            # keep track of our window
            c = s[r]
            window[c] = window.get(c, 0) + 1
            # keep track of how many characters we've used
            if c in t_chars and window[c] == t_chars[c]:
                have += 1
            # find any shorter results
            while have == need:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = (r - l + 1)
                # pop the left most element
                window[s[l]] -= 1
                if s[l] in t_chars and window[s[l]] < t_chars[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        if res_len != sys.maxsize:
            return s[l:r + 1]
        else:
            return ''
