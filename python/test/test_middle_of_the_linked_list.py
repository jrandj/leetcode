import unittest
from typing import Optional
from src.middle_of_the_linked_list import ListNode, Solution


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
    def test_a1(self):
        l1n1, l1n2, l1n3 = ListNode(1), ListNode(2), ListNode(3)
        l1n4, l1n5 = ListNode(4), ListNode(5)
        l1n1.next = l1n2
        l1n2.next = l1n3
        l1n3.next = l1n4
        l1n4.next = l1n5
        trn1, trn2, trn3 = ListNode(3), ListNode(4), ListNode(5)
        trn1.next = trn2
        trn2.next = trn3
        actual_result = Solution()
        self.assertTrue(list_equality_helper(trn1, actual_result.middleNode(l1n1)))

    def test_a2(self):
        l1n1, l1n2, l1n3 = ListNode(1), ListNode(2), ListNode(3)
        l1n4, l1n5, l1n6 = ListNode(4), ListNode(5), ListNode(6)
        l1n1.next = l1n2
        l1n2.next = l1n3
        l1n3.next = l1n4
        l1n4.next = l1n5
        l1n5.next = l1n6
        trn1, trn2, trn3 = ListNode(4), ListNode(5), ListNode(6)
        trn1.next = trn2
        trn2.next = trn3
        actual_result = Solution()
        self.assertTrue(list_equality_helper(trn1, actual_result.middleNode(l1n1)))


if __name__ == '__main__':
    unittest.main()
