import unittest
from typing import Optional
from src.construct_binary_tree_from_preorder_and_inorder_traversal import TreeNode, Solution


def tree_equality_helper(h1: Optional[TreeNode], h2: Optional[TreeNode]):
    """
    Compare 2 trees for equality.

    :param h1: The head of the first tree.
    :param h2: The head of the second tree.
    :return bool: True if equal, false otherwise.

    The time complexity is O(N) where N is the number of nodes in the tree.

    The space complexity is O(N) due to the recursion stack.
    """
    if h1 is None and h2 is None:
        return True
    elif h1 and h2 and h1.val == h2.val and tree_equality_helper(h1.left, h2.left) and \
            tree_equality_helper(h1.right, h2.right):
        return True
    else:
        return False


class Tests(unittest.TestCase):
    def test_1(self):
        # test tree
        t1n1 = TreeNode(3)
        t1n2 = TreeNode(9)
        t1n3 = TreeNode(20)
        t1n4 = TreeNode(15)
        t1n5 = TreeNode(7)
        t1n1.left = t1n2
        t1n1.right = t1n3
        t1n3.left = t1n4
        t1n3.right = t1n5

        actual_result = Solution()
        preorder = [3, 9, 20, 15, 7]
        inorder = [9, 3, 15, 20, 7]
        self.assertTrue(tree_equality_helper(t1n1, actual_result.buildTree(preorder, inorder)))

    def test_2(self):
        # test tree
        t1n1 = TreeNode(-1)

        actual_result = Solution()
        preorder = [-1]
        inorder = [-1]
        self.assertTrue(tree_equality_helper(t1n1, actual_result.buildTree(preorder, inorder)))


if __name__ == '__main__':
    unittest.main()
