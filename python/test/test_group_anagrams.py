import unittest

from src.group_anagrams import Solution
from typing import List


def list_of_lists_equality_checker(list1: List[List[str]], list2: List[List[str]]):
    """
    A list of lists equality checker where order does not matter.

    :param list1: The first list of lists for comparison.
    :type list1: List[List[Str]].
    :param list2: The second list of lists for comparison.
    :type list2: List[List[Str]].
    :return: True if the lists of lists are equal, and False otherwise.
    :rtype: Bool.
    """
    if len(list1) != len(list2):
        return False

    if all(l for l in list2 if l in list1):
        return True
    else:
        return False


class Tests(unittest.TestCase):
    def test_1(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        test_result = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        actual_result = Solution()
        self.assertTrue(list_of_lists_equality_checker(test_result, actual_result.groupAnagrams(strs)))

    def test_2(self):
        strs = [""]
        test_result = [[""]]
        actual_result = Solution()
        self.assertTrue(list_of_lists_equality_checker(test_result, actual_result.groupAnagrams(strs)))

    def test_3(self):
        strs = ["a"]
        test_result = [["a"]]
        actual_result = Solution()
        self.assertTrue(list_of_lists_equality_checker(test_result, actual_result.groupAnagrams(strs)))

    def test_4(self):
        strs = ["cab", "tin", "pew", "duh", "may", "ill", "buy", "bar", "max", "doc"]
        test_result = [["max"], ["buy"], ["doc"], ["may"], ["ill"], ["duh"], ["tin"], ["bar"], ["pew"], ["cab"]]
        actual_result = Solution()
        self.assertTrue(list_of_lists_equality_checker(test_result, actual_result.groupAnagrams(strs)))


if __name__ == "__main__":
    unittest.main()
