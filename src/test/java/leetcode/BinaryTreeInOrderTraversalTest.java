package leetcode;

import java.util.Arrays;
import java.util.List;

import org.junit.Assert;

import junit.framework.TestCase;

public class BinaryTreeInOrderTraversalTest extends TestCase {

    /**
     * The first test for BinaryTreeInorderTraversal.
     */
    public void testBinaryTreeInOrderTraversalTest1() {
        TreeNode n1 = new TreeNode(1);
        TreeNode n2 = new TreeNode(2);
        TreeNode n3 = new TreeNode(3);
        n1.setLeft(null);
        n1.setRight(n2);
        n2.setLeft(n3);
        n2.setRight(null);
        n3.setLeft(null);
        n3.setRight(null);

        List<Integer> testResult = Arrays.asList(1, 3, 2);
        BinaryTreeInorderTraversal binaryTreeInorderTraversal =
                new BinaryTreeInorderTraversal();
        List<Integer> result = binaryTreeInorderTraversal
                .inorderTraversal(n1);
        Assert.assertEquals(testResult, result);
    }

    /**
     * The second test for BinaryTreeInorderTraversal.
     */
    public void testBinaryTreeInOrderTraversalTest2() {
        List<Integer> testResult = Arrays.asList();
        BinaryTreeInorderTraversal binaryTreeInorderTraversal =
                new BinaryTreeInorderTraversal();
        List<Integer> result = binaryTreeInorderTraversal
                .inorderTraversal(null);
        Assert.assertEquals(testResult, result);
    }

    /**
     * The third test for BinaryTreeInorderTraversal.
     */
    public void testBinaryTreeInOrderTraversalTest3() {
        TreeNode n1 = new TreeNode(1);
        n1.setLeft(null);
        n1.setRight(null);

        List<Integer> testResult = Arrays.asList(1);
        BinaryTreeInorderTraversal binaryTreeInorderTraversal =
                new BinaryTreeInorderTraversal();
        List<Integer> result = binaryTreeInorderTraversal
                .inorderTraversal(n1);
        Assert.assertEquals(testResult, result);
    }

    /**
     * The fourth test for BinaryTreeInorderTraversal.
     */
    public void testBinaryTreeInOrderTraversalTest4() {
        TreeNode n1 = new TreeNode(1);
        TreeNode n2 = new TreeNode(2);
        n1.setLeft(n2);
        n1.setRight(null);
        n2.setLeft(null);
        n2.setRight(null);

        List<Integer> testResult = Arrays.asList(2, 1);
        BinaryTreeInorderTraversal binaryTreeInorderTraversal =
                new BinaryTreeInorderTraversal();
        List<Integer> result = binaryTreeInorderTraversal
                .inorderTraversal(n1);
        Assert.assertEquals(testResult, result);
    }

    /**
     * The fifth test for BinaryTreeInorderTraversal.
     */
    public void testBinaryTreeInOrderTraversalTest5() {
        TreeNode n1 = new TreeNode(1);
        TreeNode n2 = new TreeNode(2);
        n1.setLeft(null);
        n1.setRight(n2);
        n2.setLeft(null);
        n2.setRight(null);

        List<Integer> testResult = Arrays.asList(1, 2);
        BinaryTreeInorderTraversal binaryTreeInorderTraversal =
                new BinaryTreeInorderTraversal();
        List<Integer> result = binaryTreeInorderTraversal
                .inorderTraversal(n1);
        Assert.assertEquals(testResult, result);
    }

}
