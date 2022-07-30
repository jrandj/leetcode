import unittest
from src.maximum_depth_of_binary_tree import TreeNode, Solution


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
        test_result = 3
        self.assertEqual(test_result, actual_result.maxDepth(t1n1))

    def test_2(self):
        # test tree
        t1n1 = TreeNode(1)
        t1n2 = TreeNode(2)
        t1n1.right = t1n2

        actual_result = Solution()
        test_result = 2
        self.assertEqual(test_result, actual_result.maxDepth(t1n1))

    def test_3(self):
        # test tree
        actual_result = Solution()
        test_result = 0
        self.assertEqual(test_result, actual_result.maxDepth([]))

    def test_4(self):
        # test tree
        t1n1 = TreeNode(0)

        actual_result = Solution()
        test_result = 1
        self.assertEqual(test_result, actual_result.maxDepth(t1n1))


if __name__ == '__main__':
    unittest.main()
