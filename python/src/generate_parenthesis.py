from typing import List


class Solution:
    """
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
    """

    def __init__(self):
        """
        Initialise the solution.
        """
        self.res = []
        self.stack = []

    def generateParenthesis(self, n: int) -> List[str]:
        """
        Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

        The time complexity is O(4^N/(N*SQRT(N))). Faster than 97.2% of solutions.

        The space complexity is O(N) for the list and recursive function calls. Less memory than 39.47% of solutions.

        :param n: The number of pairs of parenthesis.
        :type n: Int.
        :return: All combinations of well-formed parentheses.
        :rtype: List[Str]
        """
        self.dfs(n, n)
        return self.res

    def dfs(self, open_brackets: int, close_brackets: int):
        """
        A helper method to perform a Depth-First Search (DFS).

        :param open_brackets: The number of open brackets remaining.
        :type open_brackets: Int.
        :param close_brackets: The number of close brackets remaining.
        :type close_brackets: Int.
        :return: NoneType.
        :rtype: NoneType.
        """
        # base case
        if open_brackets == close_brackets == 0:
            self.res.append("".join(self.stack))

        # we can add an opening bracket if we have not used them all
        if open_brackets > 0:
            self.stack.append("(")
            self.dfs(open_brackets - 1, close_brackets)
            self.stack.pop()

        # we can add a closing bracket if we have fewer opening brackets (we have already used some)
        if close_brackets > open_brackets:
            self.stack.append(")")
            self.dfs(open_brackets, close_brackets - 1)
            self.stack.pop()
