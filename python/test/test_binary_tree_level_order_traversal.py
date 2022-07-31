import unittest
from src.binary_tree_level_order_traversal import Solution, TreeNode


class Tests(unittest.TestCase):
    def test_1(self):
        # test case tree
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
        test_result = [[3], [9, 20], [15, 7]]
        self.assertEqual(test_result, actual_result.levelOrder(t1n1))

    def test_2(self):
        # test case tree
        t1n1 = TreeNode(1)

        actual_result = Solution()
        test_result = [[1]]
        self.assertEqual(test_result, actual_result.levelOrder(t1n1))

    def test_3(self):
        # test case tree
        t1n1 = []

        actual_result = Solution()
        test_result = []
        self.assertEqual(test_result, actual_result.levelOrder(t1n1))


if __name__ == "__main__":
    unittest.main()
