class Solution:
    def isValid(self, s: str) -> bool:
        """Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input
        string is valid.

        An input string is valid if:
            - Open brackets must be closed by the same type of brackets.
            - Open brackets must be closed in the correct order.

        :param s: The input string.
        :return bool: True if s is valid, and False otherwise.

        The time complexity is O(N) where N is the length of s. Faster than 90.82% of solutions.

        The space complexity is O(N) where N is the length of s. Less memory than 69.44% of solutions.
        """
        stack = []
        closeToOpen = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0
