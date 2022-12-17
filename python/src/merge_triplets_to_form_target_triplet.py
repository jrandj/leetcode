from typing import List


class Solution:
    """
    A triplet is an array of three integers. You are given a 2D integer array triplets, where triplets[i] = [ai, bi,
    ci] describes the ith triplet. You are also given an integer array target = [x, y, z] that describes the triplet
    you want to obtain.

    To obtain target, you may apply the following operation on triplets any number of times (possibly zero):

    Choose two indices (0-indexed) i and j (i != j) and update triplets[j] to become [max(ai, aj), max(bi, bj),
    max(ci, cj)]. For example, if triplets[i] = [2, 5, 3] and triplets[j] = [1, 7, 5], triplets[j] will be updated to
    [max(2,
    1), max(5, 7), max(3, 5)] = [2, 7, 5].

    Return true if it is possible to obtain the target triplet [x, y, z] as an element of triplets, or false otherwise.
    """

    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        """
        Return true if it is possible to obtain the target triplet [x, y, z] as an element of triplets, or false
        otherwise.

        :param triplets: A 2D integer array containing triplets.
        :type triplets: List[List[Int]].
        :param target: A target triplet.
        :type target: List[Int].
        :return: True if it is possible to obtain the target triplet [x, y, z] as an element of triplets,
        or False otherwise.
        :rtype: Bool.

        The time complexity is O(N) where N is the length of the triplets array. Faster than 42.48% of solutions.

        The space complexity is O(1) as we only use constant additional data structures. Less memory than 98.77% of
        solutions.
        """
        current_max = [0, 0, 0]
        for t in triplets:
            if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
                current_max = [max(current_max[0], t[0]), max(current_max[1], t[1]), max(current_max[2], t[2])]

        return current_max == target
