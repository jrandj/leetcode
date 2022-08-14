from typing import List


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


class Codec:
    """
    Serialization is the process of converting a data structure or object into a sequence of bits so that it can be
    stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in
    the same or another computer environment.

    Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your
    serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be
    serialized to a string and this string can be deserialized to the original tree structure.

    Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not
    necessarily need to follow this format, so please be creative and come up with different approaches yourself.

    The time complexity for both serialize and deserialize is O(N) as all nodes are visited. Faster than 49.90% of
    solutions.

    The space complexity for both serialize and deserialize is O(N) for the recursive stack. Less memory than 84.27% of
    solutions.
    """

    def __init__(self) -> None:
        self.res = []
        self.i = 0

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.

        :param root: The root of the tree to be serialized.
        :return str: The string representation of the serialized tree.
        """
        self.serialize_helper(root)
        return ",".join(self.res)

    def serialize_helper(self, node: TreeNode) -> None:
        """
        A helper for the serialize method.

        :param node:
        :param res:
        :return None.
        """
        if not node:
            self.res.append("N")
            return
        self.res.append(str(node.val))
        self.serialize_helper(node.left)
        self.serialize_helper(node.right)

    def deserialize(self, data) -> TreeNode:
        """
        Decodes your encoded data to tree.

        :param data: The string representation of a tree to be deserialized.
        :return TreeNode: The root of the serialized tree.
        """
        vals = data.split(",")
        return self.deserialize_helper(vals)

    def deserialize_helper(self, vals: List[int]) -> TreeNode:
        """
        A helper for the deserialize method.

        :param vals: The list of ints representing the tree to be deserialized.
        :return TreeNode: The root of the deserialized tree.
        """
        if vals[self.i] == "N":
            self.i += 1
            return None

        node = TreeNode(int(vals[self.i]))
        self.i += 1
        node.left = self.deserialize_helper(vals)
        node.right = self.deserialize_helper(vals)
        return node
