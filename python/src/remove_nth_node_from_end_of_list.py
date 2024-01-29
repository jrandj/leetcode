from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Given the head of a linked list, remove the nth node from the end of the list and return its head.
    """

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Given the head of a linked list, remove the nth node from the end of the list and return its head.

        :param head: The head of the linked list.
        :type head: ListNode.
        :param n: The nth element from the end to remove.
        :type n: Int.
        :return: The head of the linked list with the requested element removed.
        :rtype: ListNode.

        The time complexity is O(N). Faster than 74.53% of solutions.

        The space complexity is O(1). Less memory than 61.16% of solutions.
        """
        dummy_head = ListNode(0, head)
        l, r = dummy_head, head

        # increment the right pointer to create a gap of n
        while n > 0 and r:
            r = r.next
            n -= 1

        # move the pointers together
        while r:
            l = l.next
            r = r.next

        # remove the nth value from the end
        l.next = l.next.next

        return dummy_head.next
