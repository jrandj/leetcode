from typing import Optional, List


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
    Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder
    is the inorder traversal of the same tree, construct and return the binary tree.
    """

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and
        inorder is the inorder traversal of the same tree, construct and return the binary tree.

        :param preorder: The preorder traversal of the tree.
        :type preorder: List[int].
        :param inorder: The inorder traversal of the tree.
        :type inorder: List[int].
        :return: The root of the constructed tree.
        :rtype: TreeNode.

        The time complexity is O(N) as we iterate through the nodes once. Faster than 87.99% of solutions.

        The space complexity is O(N) due to the dictionary. Less memory than 90.47% of solutions.
        """
        preorder.reverse()
        inorder_dict = {v: i for i, v in enumerate(inorder)}
        return self.buildTree_helper(preorder, inorder_dict, 0, len(preorder) - 1)

    def buildTree_helper(self, preorder: List[int], inorder_dict: List[int], start: int, end: int) -> Optional[
        TreeNode]:
        """
        Helper method for buildTree.

        :param preorder: The preorder traversal of the tree.
        :type preorder: List[int].
        :param inorder_dict: The dictionary for fast index lookup based on value.
        :type inorder_dict: List[int].
        :param start: The starting position.
        :type start: Int.
        :param end: The ending position.
        :type end: Int.
        :return: The root of the constructed tree.
        :rtype: TreeNode.
        """
        if start > end:
            return None

        root = TreeNode(preorder.pop())
        index = inorder_dict[root.val]
        # use the index of root to split the left and right trees
        root.left = self.buildTree_helper(preorder, inorder_dict, start, index - 1)
        root.right = self.buildTree_helper(preorder, inorder_dict, index + 1, end)
        return root
