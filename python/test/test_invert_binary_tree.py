import unittest
from typing import Optional
from src.invert_binary_tree import TreeNode, Solution


def tree_equality_helper(h1: Optional[TreeNode], h2: Optional[TreeNode]):
    """
    Compare 2 trees for equality.

    :param h1: The head of the first tree.
    :type h1: TreeNode.
    :param h2: The head of the second tree.
    :type h2: TreeNode.
    :return: True if equal, false otherwise.
    :rtype: TreeNode.

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
        # test case tree
        t1n1 = TreeNode(4)
        t1n2 = TreeNode(2)
        t1n3 = TreeNode(7)
        t1n4 = TreeNode(1)
        t1n5 = TreeNode(3)
        t1n6 = TreeNode(6)
        t1n7 = TreeNode(9)
        t1n1.left = t1n2
        t1n1.right = t1n3
        t1n2.left = t1n4
        t1n2.right = t1n5
        t1n3.left = t1n6
        t1n3.right = t1n7

        # expected result
        a1n1 = TreeNode(4)
        a1n2 = TreeNode(2)
        a1n3 = TreeNode(7)
        a1n4 = TreeNode(1)
        a1n5 = TreeNode(3)
        a1n6 = TreeNode(6)
        a1n7 = TreeNode(9)
        a1n1.left = a1n3
        a1n1.right = a1n2
        a1n2.left = a1n5
        a1n2.right = a1n4
        a1n3.left = a1n7
        a1n3.right = a1n6

        actual_result = Solution()
        self.assertTrue(tree_equality_helper(a1n1, actual_result.invertTree(t1n1)))

    def test_2(self):
        # test case tree
        t1n1 = TreeNode(2)
        t1n2 = TreeNode(1)
        t1n3 = TreeNode(3)
        t1n1.left = t1n2
        t1n1.right = t1n3

        # expected result
        a1n1 = TreeNode(2)
        a1n2 = TreeNode(1)
        a1n3 = TreeNode(3)
        a1n1.left = a1n3
        a1n1.right = a1n2
        actual_result = Solution()
        self.assertTrue(tree_equality_helper(a1n1, actual_result.invertTree(t1n1)))


if __name__ == "__main__":
    unittest.main()
