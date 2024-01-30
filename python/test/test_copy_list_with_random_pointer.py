import unittest
from typing import Optional

from src.copy_list_with_random_pointer import Solution, Node


def list_equality_helper(node1: Optional[Node], node2: Optional[Node]) -> bool:
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
        l1n1, l1n2, l1n3, l1n4, l1n5 = (Node(7), Node(13), Node(11), Node(10), Node(1))
        l1n1.next = l1n2
        l1n2.next = l1n3
        l1n3.next = l1n4
        l1n4.next = l1n5
        trn1, trn2, trn3, trn4, trn5 = (Node(7), Node(13), Node(11), Node(10), Node(1))
        trn1.next = trn2
        trn2.next = trn3
        trn3.next = trn4
        trn4.next = trn5
        actual_result = Solution()
        self.assertTrue(list_equality_helper(trn1, actual_result.copyRandomList(l1n1)))


if __name__ == '__main__':
    unittest.main()
