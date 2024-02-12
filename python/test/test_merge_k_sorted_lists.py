import unittest

from typing import Optional

from src.merge_k_sorted_lists import Solution, ListNode


def list_equality_helper(node1: Optional[ListNode], node2: Optional[ListNode]) -> bool:
    """
    Compare 2 linked lists for equality.

    :param node1: The head of the first linked list.
    :type node1: ListNode.
    :param node2: The head of the second linked list.
    :type node2: ListNode.
    :return: True if equal, false otherwise.
    :rtype: Bool.

    The time complexity is O(N) where N is the overlapping length of list1 and list2.

    The space complexity is O(N) where N is the length of the combined list.
    """
    while node1 and node2:
        if node1.val != node2.val:
            return False
        node1 = node1.next
        node2 = node2.next

    if node1 or node2:
        return False

    return True


class Tests(unittest.TestCase):
    def test_1(self):
        l1n1, l1n2, l1n3 = ListNode(1), ListNode(4), ListNode(5)
        l1n1.next = l1n2
        l1n2.next = l1n3
        l2n1, l2n2, l2n3 = ListNode(1), ListNode(3), ListNode(4)
        l2n1.next = l2n2
        l2n2.next = l2n3
        l3n1, l3n2 = ListNode(2), ListNode(6)
        l3n1.next = l3n2
        trn1, trn2, trn3 = ListNode(1), ListNode(1), ListNode(2)
        trn4, trn5, trn6 = ListNode(3), ListNode(4), ListNode(4)
        trn7, trn8 = ListNode(5), ListNode(6)
        trn1.next = trn2
        trn2.next = trn3
        trn3.next = trn4
        trn4.next = trn5
        trn5.next = trn6
        trn6.next = trn7
        trn7.next = trn8
        actual_result = Solution()
        self.assertTrue(list_equality_helper(trn1, actual_result.mergeKLists([l1n1, l2n1, l3n1])))

    def test_2(self):
        actual_result = Solution()
        self.assertTrue(list_equality_helper([], actual_result.mergeKLists([])))

    def test_3(self):
        actual_result = Solution()
        self.assertTrue(list_equality_helper([], actual_result.mergeKLists([[]])))


if __name__ == '__main__':
    unittest.main()
