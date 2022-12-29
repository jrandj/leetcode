import unittest
from src.top_k_frequent_elements import Solution


class Tests(unittest.TestCase):
    def test_1a(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        test_result = [1, 2]
        actual_result = Solution()
        self.assertCountEqual(test_result, actual_result.topKFrequent_heap(nums, k))

    def test_2a(self):
        nums = [1]
        k = 1
        test_result = [1]
        actual_result = Solution()
        self.assertCountEqual(test_result, actual_result.topKFrequent_heap(nums, k))

    def test_1b(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        test_result = [1, 2]
        actual_result = Solution()
        self.assertCountEqual(test_result, actual_result.topKFrequent_bucket(nums, k))

    def test_2b(self):
        nums = [1]
        k = 1
        test_result = [1]
        actual_result = Solution()
        self.assertCountEqual(test_result, actual_result.topKFrequent_bucket(nums, k))


if __name__ == "__main__":
    unittest.main()
