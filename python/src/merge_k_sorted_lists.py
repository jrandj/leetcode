from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1: ListNode, l2: ListNode) -> Optional[ListNode]:
    """
    Helper function to merge two sorted lists.

    :param l1: The head of the first linked list.
    :type l1: ListNode.
    :param l2: The head of the second linked list.
    :type l2: ListNode.
    :return: The head of the merged linked list.
    :rtype: ListNode.

    The time complexity is O(N) where N is the length of the longest of l1 or l2.

    The space complexity is O(1).
    """
    dummy_head = ListNode(0)
    tail = dummy_head

    while l1 and l2:
        if l1.val > l2.val:
            tail.next = l2
            l2 = l2.next
        else:
            tail.next = l1
            l1 = l1.next
        tail = tail.next
    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2
    return dummy_head.next


class Solution:
    """
    You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

    Merge all the linked-lists into one sorted linked-list and return it.
    """

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

        Merge all the linked-lists into one sorted linked-list and return it.

        :param lists: The list of linked-lists.
        :type lists: List[ListNode]
        :return: The head of the merged linked list.
        :rtype: ListNode.

        The time complexity is O(N*LOG(K)) where K is the length of lists. Faster than 95.20% of solutions.

        The space complexity is O(K). Less memory than 96.88% of solutions.
        """
        # iterate through each index,
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(mergeTwoLists(l1, l2))
            # overwrite the original lists because we have merged at least 2 of them
            lists = mergedLists

        return lists[0]
