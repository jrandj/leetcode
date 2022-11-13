from typing import List, Set


class Solution:
    """
    Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated
    sequence of one or more dictionary words.

    Note that the same word in the dictionary may be reused multiple times in the segmentation.
    """

    def wordBreak_iterative(self, s: str, wordDict: List[str]) -> bool:
        """
        Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated
        sequence of one or more dictionary words.

        :param s: The input string.
        :type s: Str.
        :param wordDict: The dictionary of words.
        :type wordDict: List[Str].
        :return: True if the string can be segmented into a space-separated sequence of one or more words in wordDict,
        and False otherwise.
        :rtype: Bool.

        The time complexity is O(D^2 * K), where D is len(s) and K is len(k). Faster than 60.32% of solutions.

        The space complexity is O(N). Less memory than 94.81% of solutions.
        """
        n = len(s)
        dp = [False for i in range(n + 1)]
        dp[0] = True
        for i in range(1, n + 1):
            for w in wordDict:
                # Condition 1: Does the current word end at this index
                # Condition 2: Did a word end before the start of current word
                if dp[i - len(w)] and s[i - len(w):i] == w:
                    dp[i] = True
                    break

        return dp[-1]

    def wordBreak_recursive(self, s: str, wordDict: List[str]) -> bool:
        """
        Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated
        sequence of one or more dictionary words.

        :param s: The input string.
        :type s: Str.
        :param wordDict: The dictionary of words.
        :type wordDict: List[Str].
        :return: True if the string can be segmented into a space-separated sequence of one or more words in wordDict,
        and False otherwise.
        :rtype: Bool.

        The time complexity is O(N^3) as it is O(N) to create a substring. This results in time limit exceeded.

        The space complexity is O(N).
        """
        if not s or not wordDict:
            return False
        memo = [False] * len(s)
        return self.wordBreak_recursive_helper(s, set(wordDict), 0, memo)

    def wordBreak_recursive_helper(self, s: str, word_set: Set[str], l: int, memo: List[bool]) -> bool:
        """
        A helper method for wordBreak that is used to break the problem into smaller sub-problems.

        :param s: The input string.
        :type s: Str.
        :param word_set: The set of words from wordDict.
        :type word_set: Set[Str].
        :param l: The left index for the current substring.
        :type l: Int.
        :param memo: The memoization array.
        :type memo: List.
        :return: True if the string can be segmented into a space-separated sequence of one or more words in wordDict,
        and False otherwise.
        :rtype: Bool.
        """
        # base case
        if l == len(s):
            return True

        if memo[l] == True:
            return True

        # go to len(s) + 1 as slice end is exclusive
        for r in range(l, len(s) + 1):
            # check if candidate word s[l:r] is in the set, if so consider the smaller sub-problem
            if s[l:r] in word_set and self.wordBreak_recursive_helper(s, word_set, r, memo):
                memo[l] = True
                return True
        return False
