package leetcode;

/**
 * Helper class for list node.
 */
class ListNode {

    /** Value of the list node. */
    private int val;

    /** Pointer to the next list node. */
    private ListNode next;

    int getVal() {
        return this.val;
    }

    ListNode getNext() {
        return this.next;
    }

    void setNext(final ListNode pnext) {
        this.next = pnext;
    }

    ListNode() {
    }

    ListNode(final int pval) {
        this.val = pval;
    }

    ListNode(final int pval, final ListNode pnext) {
        this.val = pval;
        this.next = pnext;
    }
}
