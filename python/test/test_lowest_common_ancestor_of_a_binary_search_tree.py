import unittest
from src.lowest_common_ancestor_of_a_binary_search_tree import Solution, TreeNode


class Tests(unittest.TestCase):
    def test_1(self):
        # test case tree
        t1n1 = TreeNode(6)
        t1n2 = TreeNode(2)
        t1n3 = TreeNode(8)
        t1n4 = TreeNode(0)
        t1n5 = TreeNode(4)
        t1n6 = TreeNode(7)
        t1n7 = TreeNode(9)
        t1n8 = TreeNode(3)
        t1n9 = TreeNode(5)

        t1n1.left = t1n2
        t1n1.right = t1n3
        t1n2.left = t1n4
        t1n2.right = t1n5
        t1n3.left = t1n6
        t1n3.right = t1n7
        t1n5.left = t1n8
        t1n5.right = t1n9

        p, q = t1n2, t1n3
        actual_result = Solution()
        test_result = t1n1
        self.assertEqual(test_result, actual_result.lowestCommonAncestor(t1n1, p, q))

    def test_2(self):
        # test case tree
        t1n1 = TreeNode(6)
        t1n2 = TreeNode(2)
        t1n3 = TreeNode(8)
        t1n4 = TreeNode(0)
        t1n5 = TreeNode(4)
        t1n6 = TreeNode(7)
        t1n7 = TreeNode(9)
        t1n8 = TreeNode(3)
        t1n9 = TreeNode(5)

        t1n1.left = t1n2
        t1n1.right = t1n3
        t1n2.left = t1n4
        t1n2.right = t1n5
        t1n3.left = t1n6
        t1n3.right = t1n7
        t1n5.left = t1n8
        t1n5.right = t1n9

        actual_result = Solution()
        p, q = t1n2, t1n5
        test_result = t1n2
        self.assertEqual(test_result, actual_result.lowestCommonAncestor(t1n1, p, q))

    def test_3(self):
        # test case tree
        t1n1 = TreeNode(2)
        t1n2 = TreeNode(1)

        t1n1.left = t1n2

        actual_result = Solution()
        p, q = t1n1, t1n2
        test_result = t1n1
        self.assertEqual(test_result, actual_result.lowestCommonAncestor(t1n1, p, q))


if __name__ == "__main__":
    unittest.main()
