from typing import List


class Solution:
    """
    There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

    You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next
    (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

    Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit
    once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.
    """

    def canCompleteCircuit_naive(self, gas: List[int], cost: List[int]) -> int:
        """
        Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the
        circuit  once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed
        to be unique.

        :param gas: The amount of gas available.
        :type gas: List[Int].
        :param cost: The cost of the gas.
        :type cost: List[Int].
        :return: The starting gas station's index if you can travel around the circuit  once in the clockwise
        direction, otherwise return -1.
        :rtype: Int.

        The time complexity is O(N^2). Results in Time Limit Exceeded.

        The space complexity is O(1). Results in Time Limit Exceeded.
        """
        # you need enough gas!
        if sum(gas) < sum(cost):
            return -1
        for i in range(len(gas)):
            res = self.completeFromIndex(i, gas, cost)
            if res != -1:
                return res

        return -1

    def completeFromIndex(self, starting_index: int, gas: List[int], cost: List[int]) -> int:
        """
        A helper method to find the index.

        :param starting_index:
        :type starting_index:
        :param gas: The amount of gas available.
        :type gas: List[Int].
        :param cost: The cost of the gas.
        :type cost: List[Int].
        :return: If the index results in a loop, return the index.
        :rtype: Int.
        """
        idx = starting_index
        cur_gas = 0
        loop_count = 0
        # you can also use modulo here so the logic isn't as messy
        while loop_count < len(gas):
            cur_gas += gas[idx]
            # check if we can move to the next station
            if cur_gas >= cost[idx] and idx + 1 != len(gas):
                cur_gas -= cost[idx]
                idx += 1
            elif cur_gas >= cost[idx] and idx + 1 == len(gas):
                cur_gas -= cost[idx]
                idx = 0
            else:
                return -1
            loop_count += 1

        return idx

    def canCompleteCircuit_greedy(self, gas: List[int], cost: List[int]) -> int:
        """
        Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the
        circuit  once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed
        to be unique.

        :param gas: The amount of gas available.
        :type gas: List[Int].
        :param cost: The cost of the gas.
        :type cost: List[Int].
        :return: The starting gas station's index if you can travel around the circuit  once in the clockwise
        direction, otherwise return -1.
        :rtype: Int.

        The time complexity is O(N). Faster than 44.44% of solutions.

        The space complexity is O(1). Less memory than 74.45% of solutions.
        """
        # you need enough gas!
        if sum(gas) < sum(cost):
            return -1
        total = 0
        idx = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                idx = i + 1
        return idx
