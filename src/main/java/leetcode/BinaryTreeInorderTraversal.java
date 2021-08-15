package leetcode;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Stack;

/**
 * Given the root of a binary tree, return the in-order traversal of its nodes'
 * values.
 */
public class BinaryTreeInorderTraversal {

    /**
     * Given the root of a binary tree, return the in-order traversal of its
     * nodes' values.
     *
     * The time complexity O(N) as you visit each node.
     *
     * The space complexity is O(N) as you store a list of N nodes.
     *
     * @param root The root node of the binary tree.
     * @return The in-order traversal of its nodes' values.
     */
    public List<Integer> inorderTraversalRecursive(final TreeNode root) {

        if (root == null || root.getVal() < -100 || root.getVal() > 100) {
            return Collections.emptyList();
        }

        List<Integer> result = new ArrayList<>();
        visit(result, root);
        return result;

    }

    /**
     * Given the root of a binary tree, return the in-order traversal of its
     * nodes' values.
     *
     * The time complexity O(N) as you visit each node.
     *
     * The space complexity is O(N) as you store a list of N nodes.
     *
     * @param root The root node of the binary tree.
     * @return The in-order traversal of its nodes' values.
     */
    public List<Integer> inorderTraversalIterative(final TreeNode root) {

        if (root == null || root.getVal() < -100 || root.getVal() > 100) {
            return Collections.emptyList();
        }

        List<Integer> result = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        TreeNode current = root;

        // stop once we have visited all nodes
        while (current != null || !stack.isEmpty()) {
            while (current != null) {
                // traverse the LHS
                stack.add(current);
                current = current.getLeft();
            }
            // traverse the RHS
            current = stack.pop();
            result.add(current.getVal());
            current = current.getRight();
        }

        return result;

    }

    /**
     * Helper method for recursion.
     *
     * @param node   The current node.
     * @param result The array containing the traversal.
     * @return The in-order traversal of its nodes' values.
     */
    private List<Integer> visit(final List<Integer> result,
            final TreeNode node) {

        if (node != null) {
            visit(result, node.getLeft());
            result.add(node.getVal());
            visit(result, node.getRight());
        }

        return result;
    }

}
