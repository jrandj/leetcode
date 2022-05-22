package leetcode;

/**
 * Given a linked list, swap every two adjacent nodes and return its head. You
 * must solve the problem without modifying the values in the list's nodes
 * (i.e., only nodes themselves may be changed.)
 *
 */
public class SwapNodesInPairs {

    /**
     * Swap adjacent nodes in the linked list.
     *
     * The time complexity is O(N) as you are traversing the list.
     *
     * The space complexity is O(1) as we are not using any data structures.
     *
     * @param head The head of the linked list.
     * @return listNode The head of the linked list after swapping.
     */
    public ListNode swapPairs(final ListNode head) {

        if (head == null) {
            return head;
        }

        ListNode dummy = new ListNode(0);
        dummy.setNext(head);
        ListNode current = dummy;
        ListNode first;
        ListNode second;

        while (current.getNext() != null
                && current.getNext().getNext() != null) {

            if (current.getVal() < 0 || current.getVal() > 100) {
                return null;
            }

            // First node of the pair
            first = current.getNext();
            // Second node of the pair
            second = current.getNext().getNext();
            // Set the next of the first node to the node after the second node
            first.setNext(second.getNext());
            // Set the current node's next to the second node
            current.setNext(second);
            // Set the original second node to the first node
            current.getNext().setNext(first);
            // Move the current pointer two nodes ahead
            current = current.getNext().getNext();
        }
        return dummy.getNext();
    }
}
