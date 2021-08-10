package leetcode;

public class TreeNode {
    /**
     * The value of the node.
     */
    private int val;

    /**
     * The getter for the value.
     *
     * @return The value.
     */
    public int getVal() {
        return this.val;
    }

    /**
     * The setter for the value.
     *
     * @param pval The value.
     */
    public void setval(final int pval) {
        this.val = pval;
    }

    /**
     * The left node.
     */
    private TreeNode left;

    /**
     * The getter for the left node.
     *
     * @return The left node.
     */
    public TreeNode getLeft() {
        return this.left;
    }

    /**
     * The setter for the left node.
     *
     * @param pleft The left node.
     */
    public void setLeft(final TreeNode pleft) {
        this.left = pleft;
    }

    /**
     * The right node.
     */
    private TreeNode right;

    /**
     * The getter for the right node.
     *
     * @return The right node.
     */
    public TreeNode getRight() {
        return this.right;
    }

    /**
     * The setter for the right node.
     *
     * @param pright The right node.
     */
    public void setRight(final TreeNode pright) {
        this.right = pright;
    }

    /**
     * The default constructor.
     */
    TreeNode() {
    }

    /**
     * The constructor for a value.
     *
     * @param pval The value.
     */
    TreeNode(final int pval) {
        this.val = pval;
    }

    /**
     * The constructor for a value and left and right nodes.
     *
     * @param pval   The value.
     * @param pleft  The left node.
     * @param pright The right node.
     */
    TreeNode(final int pval, final TreeNode pleft, final TreeNode pright) {
        this.val = pval;
        this.left = pleft;
        this.right = pright;
    }
}
