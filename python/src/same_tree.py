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
    Given the roots of two binary trees p and q, write a function to check if they are the same or not.

    Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
    """

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Return True if the trees are equal, and False otherwise.

        :param p: The head node of the first tree.
        :type p: TreeNode.
        :param q: The head node of the second tree.
        :type q: TreeNode.
        :return: True if the trees are equal, and False otherwise.
        :rtype: Bool.

        The time complexity is O(p+q) as we visit all nodes in the tree. Faster than 37.51% of solutions.

        The space complexity is O(p+q) for the recursive stack, in the event the trees are completely unbalanced. Less
        memory than 98.34% of solutions.
        """
        # base case
        if not p and not q:
            return True
        elif not p or not q or p.val != q.val:
            return False

        # recurse
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
