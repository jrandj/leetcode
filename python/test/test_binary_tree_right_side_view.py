import unittest
from src.binary_tree_right_side_view import TreeNode, Solution


class Tests(unittest.TestCase):
    def test_1(self):
        # test tree
        t1n1 = TreeNode(1)
        t1n2 = TreeNode(2)
        t1n3 = TreeNode(3)
        t1n4 = TreeNode(5)
        t1n5 = TreeNode(4)
        t1n1.left = t1n2
        t1n1.right = t1n3
        t1n2.right = t1n4
        t1n3.right = t1n5

        actual_result = Solution()
        test_result = [1, 3, 4]
        self.assertEqual(test_result, actual_result.rightSideView(t1n1))

    def test_2(self):
        # test tree
        t1n1 = TreeNode(1)
        t1n2 = TreeNode(3)
        t1n1.right = t1n2

        actual_result = Solution()
        test_result = [1, 3]
        self.assertEqual(test_result, actual_result.rightSideView(t1n1))

    def test_3(self):
        actual_result = Solution()
        t1n1 = []
        test_result = []
        self.assertEqual(test_result, actual_result.rightSideView(t1n1))

    def test_4(self):
        # test tree
        t1n1 = TreeNode(1)
        t1n2 = TreeNode(2)
        t1n1.left = t1n2

        actual_result = Solution()
        test_result = [1, 2]
        self.assertEqual(test_result, actual_result.rightSideView(t1n1))


if __name__ == '__main__':
    unittest.main()
