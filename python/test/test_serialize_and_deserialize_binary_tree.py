import unittest
from typing import Optional
from src.serialize_and_deserialize_binary_tree import Codec, TreeNode


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
        # test case tree
        t1n1 = TreeNode(1)
        t1n2 = TreeNode(2)
        t1n3 = TreeNode(3)
        t1n4 = TreeNode(4)
        t1n5 = TreeNode(5)
        t1n1.left = t1n2
        t1n1.right = t1n3
        t1n3.left = t1n4
        t1n3.right = t1n5

        actual_result = Codec()
        test_result = t1n1
        serialised_result = actual_result.serialize(t1n1)
        deserialised_result = actual_result.deserialize(serialised_result)

        self.assertTrue(tree_equality_helper(test_result, deserialised_result))

    def test_2(self):
        # test case tree
        t1n1 = None

        actual_result = Codec()
        test_result = None
        serialised_result = actual_result.serialize(t1n1)
        deserialised_result = actual_result.deserialize(serialised_result)
        self.assertEqual(test_result, deserialised_result)


if __name__ == "__main__":
    unittest.main()
