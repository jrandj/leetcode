class Solution:
    """
    Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result
    of the evaluation.

    Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as
    eval().
    """

    def calculate(self, s: str) -> int:
        """
        Calculate the value of the expression.

        :param s: The input string representing an expression.
        :return int: The result of evaluating the expression.

        The time complexity is O(N) where N is the length of s. Faster than 78.12% of solutions.

        The space complexity is O(N) where N is the length of the stack. Less memory than 74.46% of solutions.
        """
        stack = []
        # default sign is positive
        output, cur, sign = 0, 0, 1

        if not self.valid_input(s):
            return 0

        for c in s:
            if c.isdigit():
                # build the number out of multiple digits (if applicable)
                cur = cur * 10 + int(c)
            elif c == '+':
                output += cur * sign
                sign = 1
                cur = 0
            elif c == '-':
                output += cur * sign
                sign = -1
                cur = 0
            elif c == '(':
                # store result up to now
                stack.append(output)
                # handle unary
                stack.append(sign)
                output = 0
                sign = 1
            elif c == ')':
                output += cur * sign
                # sign is added last so it is first popped
                output *= stack.pop()
                output += stack.pop()
                cur = 0
            elif c == ' ':
                # do nothing
                continue
            else:
                # input not valid
                return 0

        # handle the case of e.g. 1+1 where it does not end with )+-
        output += cur * sign
        return output

    def valid_input(self, s: str) -> bool:
        """
        Validate the input for the calculator that can be done without iteration.

        :param s: The input string representing an expression.
        :return bool: True if the input is valid, and false otherwise.
        """
        if len(s) < 1 or len(s) > int(3 * 10e5):
            return False

        return True
