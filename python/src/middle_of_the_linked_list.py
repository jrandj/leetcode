from typing import Optional


class ListNode:
    """
    Definition for singly-linked list.
    """

    def __init__(self, x):
        """
        Initialise the ListNode.

        :param x: The value of the ListNode.
        :type x: Int.
        """
        self.val = x
        self.next = None


class Solution:
    """
    Given the head of a singly linked list, return the middle node of the linked list.

    If there are two middle nodes, return the second middle node.
    """

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Given the head of a singly linked list, return the middle node of the linked list.

        :param head: The head of the linked list.
        :type head: ListNode.
        :return: The middle node of the linked list.
        :rtype: ListNode.

        The time complexity is O(N) where N is the length of the list. Faster than 92.87% of solutions.

        The space complexity is O(1). Less memory than 55.24% of solutions.
        """
        slow_pointer, fast_pointer = head, head

        # when the fast pointer reaches the end, the slow pointer will be halfway through
        while fast_pointer and fast_pointer.next:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next

        return slow_pointer
