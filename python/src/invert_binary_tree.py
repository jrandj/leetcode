from typing import Optional


class TreeNode:
    """
    Definition for a binary tree node.
    """

    def __init__(self, val=0, left=None, right=None):
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
        :return TreeNode: The root node of the inverted tree.

        The time complexity is O(N) where N is the number of nodes in the tree. Faster than 19.16% of solutions.

        The space complexity is O(1) as there are no additional data structures used. Less memory than 96.10% of
        solutions.
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
