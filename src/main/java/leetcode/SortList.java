package leetcode;

/**
 * Sort a linked list in O(n log n) time using constant space complexity.
 */
class SortList {
    /**
     * Sort a linked list.
     *
     * @param head the head of the unsorted linked list
     * @return head the head of sorted linked list
     */
    public ListNode sortList(final ListNode head) {

        // empty list or list of length 1 is already sorted
        if (head == null || head.getNext() == null) {
            return head;
        }

        ListNode temp = head;
        ListNode fast = temp;
        ListNode slow = temp;

        /*
         * Split list into halves. Head is start of lhs, temp is end of lhs.
         * Slow is start of rhs, fast is end of rhs.
         */
        while (fast != null && fast.getNext() != null) {
            temp = slow;
            slow = slow.getNext();
            fast = fast.getNext().getNext();
        }

        // temp is end of lhs so set next to null (end of rhs already null)
        temp.setNext(null);

        ListNode lhs = sortList(head);
        ListNode rhs = sortList(slow);
        return mergeLists(lhs, rhs);
    }

    /**
     * Build sorted list by merging first and second lists.
     *
     * @param pl1 the head of the first list
     * @param pl2 the head of the second list
     * @return temp.next the head of the sorted list
     */
    private ListNode mergeLists(final ListNode pl1, final ListNode pl2) {

        ListNode l1 = pl1;
        ListNode l2 = pl2;

        // dummy node to allow temp.next (currentNode used for traversal)
        ListNode temp = new ListNode(0);
        ListNode currentNode = temp;

        // build the sorted list with currentNode, increment l1 and l2 if using
        // a value
        while (l1 != null && l2 != null) {
            if (l1.getVal() < l2.getVal()) {
                currentNode.setNext(l1);
                l1 = l1.getNext();
            } else {
                currentNode.setNext(l2);
                l2 = l2.getNext();
            }
            currentNode = currentNode.getNext();
        }

        // l2 == null was reached first so l1 value remains
        if (l1 != null) {
            currentNode.setNext(l1);
            l1.getNext();
        }

        // l1 == null was reached first so l2 value remains
        if (l2 != null) {
            currentNode.setNext(l2);
            l2.getNext();
        }

        return temp.getNext();
    }
}
