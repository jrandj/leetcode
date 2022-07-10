from typing import Optional


class ListNode:
    """
    Definition for singly-linked list.
    """

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    Given the head of a singly linked list, reverse the list, and return the reversed list.

    """

    def reverseList_iterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
         Given the head of a singly linked list, reverse the list, and return the reversed list.

        :param head: The head of the linked list.
        :return ListNode: The head of the reversed linked list.

        The time complexity is O(N) where N is the length of the list. Faster than 7.86% of solutions.

        The space complexity is O(1). Less memory than 28.35% of solutions.

        """
        prev, tail = None, head

        while tail:
            # store the original next node before you overwrite it
            temp = tail.next
            # set the next node to be the previous node
            tail.next = prev
            # point prev to current node for next use
            prev = tail
            # progress through the list
            tail = temp

        # prev contains the last tail
        return prev

    def reverseList_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Given the head of a singly linked list, reverse the list, and return the reversed list.

        :param head: The head of the linked list.
        :return ListNode: The head of the reversed linked list.

        The time complexity is O(N) where N is the length of the list. Faster than 23.64% of solutions.

        The space complexity is O(N) due to the function stack from recursion. Less memory than 16.77% of solutions.

        """
        # trivial case
        if head is None:
            return None
        # base case
        elif head.next is None:
            return head
        else:
            tail = head.next
            # disconnect
            head.next = None
            remaining = self.reverseList_recursive(tail)
            tail.next = head
            return remaining
