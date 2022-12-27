class Solution:
    """
    Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

    The following rules define a valid string:
        - Any left parenthesis '(' must have a corresponding right parenthesis ')'.
        - Any right parenthesis ')' must have a corresponding left parenthesis '('.
        - Left parenthesis '(' must go before the corresponding right parenthesis ')'.
        - '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
    """

    def checkValidString(self, s: str) -> bool:
        """
        Return True if s is a valid parenthesis string, and False otherwise.

        :param s: The input string.
        :type s: Str.
        :return: True if s is a valid parenthesis string, and False otherwise.
        :rtype: Bool.

        The time complexity is O(N) as we iterate through s. Faster than 82.54% of solutions.

        The space complexity is O(N) for the stacks. Less memory than 29.1% of solutions.
        """
        opening_brackets = []
        stars = []

        for i, val in enumerate(s):
            if val == "(":
                opening_brackets.append(i)
            elif val == ")":
                if opening_brackets:
                    opening_brackets.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
            # we know this must be *
            else:
                stars.append(i)

        while opening_brackets and stars:
            # the index of opening must not be greater than index of *
            if opening_brackets[-1] > stars[-1]:
                return False

            opening_brackets.pop()
            stars.pop()

        return len(opening_brackets) == 0

    def checkValidString_greedy(self, s: str) -> bool:
        """
        Return True if s is a valid parenthesis string, and False otherwise.

        This is the greedy solution.

        :param s: The input string.
        :type s: Str.
        :return: True if s is a valid parenthesis string, and False otherwise.
        :rtype: Bool.

        The time complexity is O(N) as we iterate through s. Faster than 74.93% of solutions.

        The space complexity is O(1) as we don't use any additional data structures. Less memory than 98.76% of
        solutions.
        """
        left_min, left_max = 0, 0

        for c in s:
            if c == "(":
                left_min, left_max = left_min + 1, left_max + 1
            elif c == ")":
                left_min, left_max = left_min - 1, left_max - 1
            # we know this must be *
            else:
                left_min, left_max = left_min - 1, left_max + 1

            if left_max < 0:
                return False
            # handle string like ( * ) (
            if left_min < 0:
                left_min = 0

        return left_min == 0
