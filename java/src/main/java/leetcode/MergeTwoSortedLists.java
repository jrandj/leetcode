package leetcode;

/**
 * Merge two sorted linked lists and return it as a new list. The new list
 * should be made by splicing together the nodes of the first two lists.
 *
 * Example:
 *
 * Input: 1->2->4, 1->3->4 Output: 1->1->2->3->4->4
 */
final class MergeTwoSortedLists {

    private MergeTwoSortedLists() {
        // prevent instantiation
    }

    /**
     * Merge two sorted linked lists and return the results in a new list.
     *
     * @param l1 the head of the first sorted list
     * @param l2 the head of the second sorted list
     * @return head the head of the merged list
     */
    public static ListNode mergeTwoLists(final ListNode l1, final ListNode l2) {
        ListNode head = new ListNode(0);
        ListNode p = head;
        ListNode p1 = l1;
        ListNode p2 = l2;

        while (p1 != null && p2 != null) {
            // add the smallest ones first
            if (p1.getVal() < p2.getVal()) {
                p.setNext(p1);
                p1 = p1.getNext();
            } else {
                p.setNext(p2);
                p2 = p2.getNext();
            }
            p = p.getNext();

        }

        if (p1 != null) {
            p.setNext(p1);
        }

        if (p2 != null) {
            p.setNext(p2);
        }
        return head.getNext();
    }
}
