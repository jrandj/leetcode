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
    Given head, the head of a linked list, determine if the linked list has a cycle in it.

    There is a cycle in a linked list if there is some node in the list that can be reached again by continuously
    following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is
    connected to. Note that pos is not passed as a parameter.

    Return True if there is a cycle in the linked list. Otherwise, return False.
    """

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Return True if there is a cycle in the linked list. Otherwise, return False.

        :param head: The head of the linked list.
        :return bool: True if there is a cycle in the linked list, and False otherwise.

        The time complexity is O(N) where N is the length of the list. Faster than 22.82% of solutions.

        The space complexity is O(1). Less memory than 66.33% of solutions.

        """
        fast_pointer, slow_pointer = head, head

        while fast_pointer and fast_pointer.next:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next

            if fast_pointer == slow_pointer:
                return True

        return False
