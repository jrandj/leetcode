package leetcode;

/**
 * You are given two non-empty linked lists representing two non-negative
 * integers. The digits are stored in reverse order and each of their nodes
 * contain a single digit. Add the two numbers and return it as a linked list.
 * You may assume the two numbers do not contain any leading zero, except the
 * number 0 itself.
 */
public final class AddTwoNumbers {

    private AddTwoNumbers() {
        // prevent instantiation
    }

    /**
     * This method checks if the array is empty.
     *
     * @param pl1 the first array
     * @param pl2 the second array
     * @return the head node of a list containing sum
     */
    public static ListNode addTwoNumbersSolution(final ListNode pl1,
            final ListNode pl2) {
        ListNode l1 = pl1;
        ListNode l2 = pl2;
        ListNode dummyHead = new ListNode(0);
        ListNode l3 = dummyHead;
        int l1Val;
        int l2Val;
        int sum;
        int carry = 0;
        int digit = 0;

        while (l1 != null || l2 != null) {

            if (l1 != null) {
                l1Val = l1.getVal();
            } else {
                l1Val = 0;
            }

            if (l2 != null) {
                l2Val = l2.getVal();
            } else {
                l2Val = 0;
            }

            sum = l1Val + l2Val + carry;
            carry = sum / 10;
            digit = sum % 10;
            ListNode newNode = new ListNode(digit);
            l3.setNext(newNode);

            if (l1 != null) {
                l1 = l1.getNext();
            }
            if (l2 != null) {
                l2 = l2.getNext();
            }
            l3 = l3.getNext();
        }

        if (carry > 0) {
            ListNode newNode = new ListNode(carry);
            l3.setNext(newNode);
            l3 = l3.getNext();
        }
        return dummyHead.getNext();
    }
}
