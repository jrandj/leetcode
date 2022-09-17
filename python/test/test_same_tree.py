import unittest
from typing import Optional
from src.same_tree import TreeNode, Solution


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
        t1n1 = TreeNode(1)
        t1n2 = TreeNode(2)
        t1n3 = TreeNode(3)
        t1n1.left = t1n2
        t1n1.right = t1n3
        t2n1 = TreeNode(1)
        t2n2 = TreeNode(2)
        t2n3 = TreeNode(3)
        t2n1.left = t2n2
        t2n1.right = t2n3
        actual_result = Solution()
        self.assertTrue(actual_result.isSameTree(t1n1, t2n1))

    def test_2(self):
        t1n1 = TreeNode(1)
        t1n2 = TreeNode(2)
        t1n1.left = t1n2
        t2n1 = TreeNode(1)
        t2n2 = TreeNode(2)
        t2n1.right = t2n2
        actual_result = Solution()
        self.assertFalse(actual_result.isSameTree(t1n1, t2n1))

    def test_3(self):
        t1n1 = TreeNode(1)
        t1n2 = TreeNode(2)
        t1n3 = TreeNode(1)
        t1n1.left = t1n2
        t1n1.right = t1n3
        t2n1 = TreeNode(1)
        t2n2 = TreeNode(1)
        t2n3 = TreeNode(2)
        t2n1.left = t2n2
        t2n1.right = t2n3
        actual_result = Solution()
        self.assertFalse(actual_result.isSameTree(t1n1, t2n1))


if __name__ == '__main__':
    unittest.main()
