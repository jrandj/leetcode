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
    Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

    According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and
    q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of
    itself).”
    """

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

        :param root: The root node of the tree.
        :type root: TreeNode.
        :param p: The first node for determining LCA.
        :type p: TreeNode.
        :param q: The second node for determining LCA.
        :type q: TreeNode.
        :return: The LCA.
        :rtype: TreeNode.

        The time complexity is O(N) as we traverse the tree. Faster than 96.91% of solutions.

        The space complexity is O(N) due to the recursion. Less memory than 22.85% of solutions.
        """
        cur = root
        # p and q must exist in the tree
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur
