from typing import List


class Solution:
    """
    Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size
    groupSize, and consists of groupSize consecutive cards.

    Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return
    true if she can rearrange the cards, or false otherwise.
    """

    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return
        true if she can rearrange the cards, or false otherwise.

        :param hand: An array of cards.
        :type hand: List[Int].
        :param groupSize: The size of the groups.
        :type groupSize: Int.
        :return: True if the cards can be rearranged, and False otherwise.
        :rtype: Bool.

        The time complexity is O(N*N/groupSize) where N is the length of the hand. Faster than 91.85% of solutions.

        The space complexity is O(N) for the dict. Less memory than 76.55% of solutions.
        """
        if len(hand) % groupSize:
            return False

        hand.sort()
        n = len(hand)
        count = {}
        for num in hand:
            count[num] = 1 + count.get(num, 0)

        for i in range(n):
            # select the current element
            if count.get(hand[i], 0) != 0:
                count[hand[i]] -= 1
                # try and make a sequence up to groupSize
                for j in range(hand[i] + 1, hand[i] + groupSize):
                    # if we don't have count[j] there will be a gap in the subset
                    if count.get(j, 0) == 0:
                        return False
                    count[j] -= 1

        return True
