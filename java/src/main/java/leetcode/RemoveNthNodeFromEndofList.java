package leetcode;

/**
 * Given a linked list, remove the n-th node from the end of list and return its
 * head.
 *
 * Example: Given linked list: 1->2->3->4->5, and n = 2. After removing the
 * second node from the end, the linked list becomes 1->2->3->5. Note: Given n
 * will always be valid.
 *
 * Follow up: Could you do this in one pass?
 */
final class RemoveNthNodeFromEndofList {

    private RemoveNthNodeFromEndofList() {
        // prevent instantiation
    }

    /**
     * Remove the n-th node from the end of the list and return the head.
     *
     * @param head the linked list head node
     * @param n    the n'th node
     * @return head the linked list head node
     */
    public static ListNode removeNthFromEnd(final ListNode head, final int n) {
        ListNode dummyHead = new ListNode(0);
        dummyHead = head;
        int i = 0;

        int len = counter(head, n);
        int index = len - n;

        if (head == null || index < 0) {
            return null;
        }

        if (index == 0) {
            return head.getNext();
        }

        while (dummyHead != null) {
            // want to skip at "the one before"
            if (i == index - 1) {
                dummyHead.setNext(dummyHead.getNext().getNext());
            }
            dummyHead = dummyHead.getNext();
            i++;
        }

        return head;
    }

    /**
     * Count the number of elements in a linked list.
     *
     * @param head the linked list head node
     * @param n    the n'th node
     * @return len the length of the linked list
     */
    public static int counter(final ListNode head, final int n) {
        ListNode dummyHead = new ListNode(0);
        dummyHead.setNext(head);
        int len = 0;
        while (dummyHead.getNext() != null) {
            dummyHead = dummyHead.getNext();
            len++;
        }

        return len;
    }
}
