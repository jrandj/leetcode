import unittest

from src.merge_triplets_to_form_target_triplet import Solution


class Tests(unittest.TestCase):
    def test_1(self):
        triplets = [[2, 5, 3], [1, 8, 4], [1, 7, 5]]
        target = [2, 7, 5]
        actual_result = Solution()
        self.assertTrue(actual_result.mergeTriplets(triplets, target))

    def test_2(self):
        triplets = [[3, 4, 5], [4, 5, 6]]
        target = [3, 2, 5]
        actual_result = Solution()
        self.assertFalse(actual_result.mergeTriplets(triplets, target))

    def test_3(self):
        triplets = [[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]]
        target = [5, 5, 5]
        actual_result = Solution()
        self.assertTrue(actual_result.mergeTriplets(triplets, target))


if __name__ == "__main__":
    unittest.main()
