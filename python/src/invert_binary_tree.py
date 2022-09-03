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
    Given the root of a binary tree, invert the tree, and return its root.
    """

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Given the root of a binary tree, invert the tree, and return its root.

        :param root: The root node of the input tree.
        :type root: TreeNode.
        :return: The root node of the inverted tree.
        :rtype: TreeNode.
        """
        if not root:
            return None

        # swap left and right nodes
        tmp = root.right
        root.right = root.left
        root.left = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
