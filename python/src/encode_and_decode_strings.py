from typing import List


class Solution:
    """
    Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and
    is decoded back to the original list of strings.
    """

    def encode(self, strings: List[str]) -> str:
        """
        Encode a string for transmission.

        :param strings: The list of strings for encoding.
        :type strings: List[Str].
        :return: The encoded string.
        :rtype: Str.

        The time complexity is O(N) where N is the length of strings.

        The space complexity is O(1) as we don't use any additional data structures.
        """
        # res = ""
        output_list = []
        for s in strings:
            # strings are immutable so this approach creates a new string each time
            # res += str(len(s)) + "~" + s
            output_list.append(str(len(s)) + "~" + s)

        res = "".join(output_list)
        return res

    def decode(self, s: str) -> List[str]:
        """
        Decode a string from transmission.

        :param s: The string for decoding.
        :type s: Str.
        :return: The decoded list of strings.
        :rtype: List[Str].

        The time complexity is O(N) where N is the length of s.

        The space complexity is O(1) as we don't use any additional data structures.
        """
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "~":
                j += 1
            # j equals ~ so the number is from i:j
            length = int(s[i:j])
            # the string comes after ~ (j + 1) and goes until length (length is inclusive)
            res.append(s[j + 1: j + 1 + length])
            # the previous string ends at j + 1 + length, so we skip past that
            i = j + 1 + length
        return res
