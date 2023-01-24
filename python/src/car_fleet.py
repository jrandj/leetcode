from typing import List


class Solution:
    """
    There are n cars going to the same destination along a one-lane road. The destination is target miles away.

    You are given two integer array position and speed, both of length n, where position[i] is the position of the ith
    car and speed[i] is the speed of the ith car (in miles per hour).

    A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same
    speed. The faster car will slow down to match the slower car's speed. The distance between these two cars is
    ignored (i.e., they are assumed to have the same position).

    A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is
    also a car fleet.

    If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

    Return the number of car fleets that will arrive at the destination.
    """

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Return the number of car fleets that will arrive at the destination.

        :param target: The distance to the target in miles.
        :type target: Int.
        :param position: The current positions of the cars.
        :type position: List[Int].
        :param speed: The current speeds of the cars.
        :type speed: List[Int].
        :return: The number of car fleets.
        :rtype: List[Int].

        The time complexity is O(N*LOG(N)) as we sort the input. Faster than 29.55% of solutions.

        The space complexity is O(N) to store the pairs. Less memory than 99.50% of solutions.
        """
        # start from cars closest to target
        pairs = [(position[i], speed[i]) for i in range(len(position))]
        fleets = cur_time = 0
        for dist, speed in sorted(pairs, reverse=True):
            destination_time = (target - dist) / speed
            # if we beat the destination_time we should get there faster so will create a fleet
            if cur_time < destination_time:
                fleets += 1
                cur_time = destination_time

        return fleets
