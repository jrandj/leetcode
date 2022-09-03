from typing import Optional


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
    Given the root of a binary tree, return its maximum depth.

    A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest
    leaf node.
    """

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Given the root of a binary tree, return its maximum depth.

        :param root: The root node of the tree.
        :type root: TreeNode.
        :return: The maximum depth of the tree.
        :rtype: Int.

        The time complexity is O(N) as we visit all nodes. Faster than 23.32% of solutions.

        The space complexity is O(N) for the recursive call stack. Less memory than 54.91% of solutions.
        """
        if not root:
            return 0

        # builds up from 1 at the bottom level
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
