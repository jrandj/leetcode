class Solution:
    """
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using
    all the original letters exactly once.
    """

    def isAnagram(self, s: str, t: str) -> bool:
        """
        Given two strings s and t, return true if t is an anagram of s, and false otherwise.

        :param s: The first string.
        :type s: Str.
        :param t: The second string.
        :type t: Str.
        :return: True if t is an anagram of s, and False otherwise.
        :rtype: Bool.

        The time complexity is O(t + s) as we iterate through both. Faster than 25.65% of solutions.

        The space complexity is O(s) for the dict. Less memory than 96.94% of solutions.

        Both strings could also be sorted and compared, this would have a time complexity of O(s LOG(s) + t LOG(t) and
        use some memory depending on the sorting algorithm, so overall is not a better solution but possibly trading
        time complexity for space complexity.
        """
        # handle the trivial case
        if len(s) != len(t):
            return False

        dict = {}  # character : count

        for c in s:
            # safely check if c is a key already
            dict[c] = 1 + dict.get(c, 0)

        for c in t:
            if c in dict.keys():
                dict[c] -= 1
            else:
                return False

        # check if all values are 0 (they have all been used)
        return all(value == 0 for value in dict.values())
