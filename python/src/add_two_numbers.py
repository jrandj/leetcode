from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse
    order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.
    """

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Add the numbers represented by linked lists with heads l1 and l2.

        :param l1: The head of the first linked list.
        :type l1: ListNode.
        :param l2: The head of the second linked list.
        :type l2: ListNode.
        :return: The head of the list node representing the sum.
        :rtype: ListNode.

        The time complexity is O(N) to iterate through each list. Faster than 61.85% of solutions.

        The space complexity is O(N) to store the new linked list. Less memory than 51.33% of solutions.
        """
        dummy_head = ListNode(0)
        cur = dummy_head
        carry = 0

        while l1 or l2 or carry:
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0

            # calculate the value for this position
            node_value = l1val + l2val + carry
            carry = node_value // 10
            val = node_value % 10
            cur.next = ListNode(val)

            # increment the pointers
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            cur = cur.next

        return dummy_head.next
