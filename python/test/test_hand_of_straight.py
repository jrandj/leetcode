from src.hand_of_straights import Solution

import unittest


class Tests(unittest.TestCase):
    def test_1(self):
        hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
        groupSize = 3
        actual_result = Solution()
        self.assertTrue(actual_result.isNStraightHand(hand, groupSize))

    def test_2(self):
        hand = [1, 2, 3, 4, 5]
        groupSize = 4
        actual_result = Solution()
        self.assertFalse(actual_result.isNStraightHand(hand, groupSize))


if __name__ == "__main__":
    unittest.main()
