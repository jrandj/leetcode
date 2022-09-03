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
    Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right,
    level by level).
    """

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right,
        level by level).

        :param root: The root node of the tree.
        :type root: TreeNode.
        :return: The level order traversal.
        :rtype: List[List[int]].

        The time complexity is O(N) as we traverse the tree once. Faster than 44.91% of solutions.

        The space complexity is O(N) for the queue. Less memory than 85.03% of solutions.
        """
        res = []
        dq = deque()
        dq.append(root)

        while dq:
            dq_len = len(dq)
            level = []
            for i in range(dq_len):
                node = dq.popleft()
                if node:
                    level.append(node.val)
                    dq.append(node.left)
                    dq.append(node.right)
            if level:
                res.append(level)

        return res
