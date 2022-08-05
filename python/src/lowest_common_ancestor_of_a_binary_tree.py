class TreeNode:
    """
    Definition for a binary tree node.
    """

    def __init__(self, val=0, left=None, right=None):
        """
        Initialise a Tree.

        :param val: The value of the node.
        :param left: The node to the left of the current node.
        :param right: The node to the right of the current node.
        """
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

    According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as
    the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
    """

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

        :param cur: The root node of the tree.
        :param p: The first node for determining LCA.
        :param q: The second node for determining LCA.
        :return TreeNode: The LCA.

        The time complexity is O(N) as we traverse the tree. Faster than 84.90% of solutions.

        The space complexity is O(N) for the function stack. Less memory than 63.87% of solutions.
        """
        return self.dfs(root, p, q)

    def dfs(self, cur: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Helper method to find the LCA.

        :param cur: The current node of the tree.
        :param p: The first node for determining LCA.
        :param q: The second node for determining LCA.
        :return TreeNode: The LCA.
        """
        # return when we hit a leaf node
        if not cur:
            return None

        # we can't go any lower for an LCA in this case
        if cur == p or cur == q:
            return cur

        # traverse the tree
        left = self.dfs(cur.left, p, q)
        right = self.dfs(cur.right, p, q)

        # scenario #1 - cur is the LCA
        if left and right:
            return cur

        # scenario #2 - left or right is the LCA
        return left if left else right
