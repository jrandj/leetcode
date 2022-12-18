from src.partition_labels import Solution

import unittest


class Tests(unittest.TestCase):
    def test_1(self):
        s = "ababcbacadefegdehijhklij"
        test_result = [9, 7, 8]
        actual_result = Solution()
        self.assertCountEqual(test_result, actual_result.partitionLabels(s))

    def test_2(self):
        s = "eccbbbbdec"
        test_result = [10]
        actual_result = Solution()
        self.assertCountEqual(test_result, actual_result.partitionLabels(s))


if __name__ == "__main__":
    unittest.main()
