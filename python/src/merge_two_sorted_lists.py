from typing import Optional


class ListNode:
    """
    Definition for singly-linked list.
    """

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    You are given the heads of two sorted linked lists list1 and list2.

    Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first 
    two lists.

    Return the head of the merged linked list.
    """

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge the two lists in a one sorted list.

        :param list1: The head of the first sorted linked list.
        :param list2: The head of the second sorted linked list.
        :return ListNode: The head of the merged linked list.

        The time complexity is O(N) where N is the overlapping length of list1 and list2. Faster than 14.89% of
        solutions.

        The space complexity is O(N) where N is the length of the combined list. Less memory than 78.99% of solutions.

        """
        dummy_head = ListNode()
        tail = dummy_head

        while list1 and list2:
            # input constraints
            if list1.val < -100 or list2.val < -100 or list1.val > 100 or list2.val > 100:
                return None

            # build combined list with tail
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy_head.next
