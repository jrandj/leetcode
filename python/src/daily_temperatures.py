from typing import List


class Solution:
    """
    Given an array of integers temperatures represents the daily temperatures, return an array answer such that
    answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no
    future day for which this is possible, keep answer[i] == 0 instead.
    """

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Given an array of integers temperatures represents the daily temperatures, return an array answer such that
        answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no
        future day for which this is possible, keep answer[i] == 0 instead.

        :param: temperatures: An array of integers representing the daily temperature.
        :type: temperatures: List[Int].
        :return: An array of integers where res[i] is the numbr of days you have to wait for a warmer temperature.
        :rtype: List[Int].

        The time complexity is O(N) where N is the length of the temperatures array. Faster than 91.98% of solutions.

        The space complexity is O(N) for the stack. Less memory than 69.79% of solutions.
        """
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            # add to the stack unless the temp is greater than the top of the stack
            while stack and t > temperatures[stack[-1]]:
                stack_i = stack.pop()
                # store the days difference between the current temp (which is warmer than popped element)
                res[stack_i] = i - stack_i

            stack.append(i)
        return res
