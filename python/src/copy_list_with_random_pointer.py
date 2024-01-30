# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    """
    A linked list of length n is given such that each node contains an additional random pointer, which could point
    to any node in the list, or null.

    Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node
    has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes
    should point to new nodes in the copied list such that the pointers in the original list and copied list represent
    the same list state. None of the pointers in the new list should point to nodes in the original list.

    For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding
    two nodes x and y in the copied list, x.random --> y.

    Return the head of the copied linked list.
    """

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Return the head of the copied linked list.

        :param head: The head of the linked list.
        :type head: Node.
        :return: The head of the copied linked list.
        :rtype: Node.

        The time complexity is O(N) to iterate through the list. Faster than 80.94% of solutions.

        The space complexity is O(N) for the hash map. Less memory than 80.55% of solutions.
        """
        # keep a mapping so that we can update the new nodes on second pass
        old_to_new = {None: None}

        # iterate through the list creating the new nodes
        cur = head
        while cur:
            new_node = Node(cur.val)
            old_to_new[cur] = new_node
            cur = cur.next

        # iterate through the list updating the references
        cur = head
        while cur:
            new_node = old_to_new[cur]
            new_node.next = old_to_new[cur.next]
            new_node.random = old_to_new[cur.random]
            cur = cur.next

        return old_to_new[head]
