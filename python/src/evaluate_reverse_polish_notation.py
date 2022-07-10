from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Evaluate the value of an arithmetic expression in Reverse Polish Notation.

        Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

        Note that division between two integers should truncate toward zero.

        It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a
        result, and there will not be any division by zero operation.

        :param tokens: The list of tokens.
        :return int: The result of evaluating the expression.

        The time complexity is O(N) where N is the length of tokens. Faster than 99.99% of solutions.

        The space complexity is O(N) where N is the length of tokens. Less memory than 56.76% of solutions.
        """
        stack = []

        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(c))

        return stack[0]
