import unittest
from typing import Optional

from src.linked_list_cycle import Solution, ListNode


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
        l1n1, l1n2, l1n3, l1n4 = ListNode(3), ListNode(2), ListNode(0), ListNode(-4)
        l1n1.next = l1n2
        l1n2.next = l1n3
        l1n3.next = l1n4
        l1n4.next = l1n2
        test_result = True
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.hasCycle(l1n1))

    def test_a2(self):
        l1n1, l1n2 = ListNode(1), ListNode(2)
        l1n1.next = l1n2
        l1n2.next = l1n1
        test_result = True
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.hasCycle(l1n1))

    def test_a3(self):
        l1n1 = ListNode(1)
        test_result = False
        actual_result = Solution()
        self.assertEqual(test_result, actual_result.hasCycle(l1n1))


if __name__ == '__main__':
    unittest.main()
