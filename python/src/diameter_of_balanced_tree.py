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
    Given the root of a binary tree, return the length of the diameter of the tree.

    The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

    The length of a path between two nodes is represented by the number of edges between them.
    """

    def __init__(self):
        """
        Initialise the diameter property. This is tracked here so that we don't need to pass it to the height method.
        """
        self.diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Given the root of a binary tree, return the length of the diameter of the tree.

        :param root: The root node of the tree.
        :type root: TreeNode.
        :return: The length of the path between two nodes.
        :rtype: Int.

        The time complexity is O(N) as we visit all nodes in the tree. Faster than 34.91% of solutions.

        The space complexity is O(N) due to the recursive stack. Less memory than 42.54% of solutions.
        """
        if root is None:
            return 0

        self.height(root)
        return self.diameter

    def height(self, root: Optional[TreeNode]) -> int:
        """
        Return the height of the deepest subtree of root.

        :param root: The root node of the tree.
        :type root: TreeNode.
        :return: The height of the deepest subtree of root.
        :rtype: Int.
        """
        if root is None:
            return 0

        # recurse to the bottom of the tree
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        # store the current diameter if it is larger
        self.diameter = max(self.diameter, left_height + right_height)
        # return the height of the deepest subtree of root (add 1 for current node)
        return max(left_height, right_height) + 1
