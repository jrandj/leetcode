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
    Given a binary tree, determine if it is height-balanced.

    For this problem, a height-balanced binary tree is defined as a binary tree in which the left and right subtrees
    of every node differ in height by no more than 1.
    """

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Given a binary tree, determine if it is height-balanced.

        :param root: The root of the tree.
        :type root: TreeNode.
        :return: True if the tree is height balanced, and False otherwise.
        :rtype: Bool.
        """
        if root is None:
            return True

        # recurse down to the bottom nodes
        if self.isBalanced(root.left) and self.isBalanced(root.right):
            left_height = self.height(root.left)
            right_height = self.height(root.right)

            # check balanced condition
            if abs(left_height - right_height) <= 1:
                return True

        return False

    def height(self, root: Optional[TreeNode]) -> int:
        """
        Calculate the height of a tree.

        :param root: The root node of the tree.
        :type root: TreeNode.
        :return: The height of the tree.
        :rtype: Int.
        """
        if root is None:
            return 0

        # add 1 to the height because a tree is of at least height 1
        return max(self.height(root.left), self.height(root.right)) + 1
