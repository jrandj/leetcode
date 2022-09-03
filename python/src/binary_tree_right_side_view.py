from typing import Optional, List
from collections import deque


class TreeNode:
    """
    Definition for a binary tree node.
    """

    def __init__(self, val=0, left=None, right=None):
        """
        Initialise a Tree.

        :param val: The value of the node.
        :type val: Int.
        :param left: The node to the left of the current node.
        :type left: TreeNode, NoneType.
        :param right: The node to the right of the current node.
        :type right: TreeNode, NoneType.
        """
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes
    you can see ordered from top to bottom.
    """

    def __init__(self):
        """
        Track the result here so that we don't need to pass it around.
        """
        self.res = []

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes
        you can see ordered from top to bottom.

        :param root: The root node for the tree.
        :type root: TreeNode.
        :return: The right side path.
        :rtype: List[int].

        The time complexity is O(N) as we visit every node in the tree. Faster than 56.48% of solutions.

        The space complexity is O(N) for the queue. Less memory than 70.23% of solutions.
        """
        q = deque()
        q.append(root)
        res = []

        # bfs to find RHS of each level
        while q:
            rhs = None
            q_len = len(q)
            for i in range(q_len):
                node = q.popleft()
                if node:
                    # track rightmost node in level
                    rhs = node
                    q.append(node.left)
                    q.append(node.right)

            # add rightmost node value to result
            if rhs:
                res.append(rhs.val)

        return res
