class Solution:
    """
    Given a string s, find the length of the longest substring without repeating characters.
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Given a string s, find the length of the longest substring without repeating characters.

        :param s: The input string.
        :type s: Str.
        :return: The longest substring without repeating characters.
        :rtype: Int.

        The time complexity is O(N) as we iterate over s. Faster than 87.05% of solutions.

        The space complexity is O(N) for the set. Less memory than 49.44% of solutions.
        """
        left_index = 0
        char_set = set()
        longest_candidate = 0

        # window approach
        for right_index, right_char in enumerate(s):

            # skip over duplicates
            while right_char in char_set:
                char_set.remove(s[left_index])
                left_index += 1

            char_set.add(right_char)
            candidate_length = right_index - left_index + 1
            longest_candidate = max(longest_candidate, candidate_length)

        return longest_candidate
