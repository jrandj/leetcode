package leetcode;

import junit.framework.Assert;
import junit.framework.TestCase;
import leetcode.AddTwoNumbers.ListNode;

public class InsertionSortListTest extends TestCase {
    /**
     * The first test for InsertionSortList.
     *
     */
    public void testInsertionSortList1() {
        ListNode l1n1 = new ListNode(4);
        ListNode l1n2 = new ListNode(2);
        ListNode l1n3 = new ListNode(1);
        ListNode l1n4 = new ListNode(3);
        l1n1.next = l1n2;
        l1n2.next = l1n3;
        l1n3.next = l1n4;

        ListNode l2n1 = new ListNode(1);
        ListNode l2n2 = new ListNode(2);
        ListNode l2n3 = new ListNode(3);
        ListNode l2n4 = new ListNode(4);
        l2n1.next = l2n2;
        l2n2.next = l2n3;
        l2n3.next = l2n4;

        InsertionSortList instance = new InsertionSortList();
        ListNode actualResult = instance.insertionSortList(l1n1);
        Assert.assertTrue(compareLists(actualResult, l2n1));
    }

    /**
     * The second test for InsertionSortList.
     *
     */
    public void testInsertionSortList2() {
        ListNode l1n1 = new ListNode(-1);
        ListNode l1n2 = new ListNode(5);
        ListNode l1n3 = new ListNode(3);
        ListNode l1n4 = new ListNode(4);
        ListNode l1n5 = new ListNode(0);
        l1n1.next = l1n2;
        l1n2.next = l1n3;
        l1n3.next = l1n4;
        l1n4.next = l1n5;

        ListNode l2n1 = new ListNode(-1);
        ListNode l2n2 = new ListNode(0);
        ListNode l2n3 = new ListNode(3);
        ListNode l2n4 = new ListNode(4);
        ListNode l2n5 = new ListNode(5);
        l2n1.next = l2n2;
        l2n2.next = l2n3;
        l2n3.next = l2n4;
        l2n4.next = l2n5;

        InsertionSortList instance = new InsertionSortList();
        ListNode actualResult = instance.insertionSortList(l1n1);
        Assert.assertTrue(compareLists(actualResult, l2n1));
    }

    /**
     * Helper method to compare lists.
     *
     * @param headA The head of the first list
     * @param headB The head of the second list
     * @return true if the lists are equal and false otherwise
     */
    boolean compareLists(final ListNode headA, final ListNode headB) {
        if ((headA == null) ^ (headB == null)) {
            return false;
        }

        if ((headA == null) && (headB == null)) {
            return true;
        }

        if (headA.val != headB.val) {
            return false;
        }

        return compareLists(headA.next, headB.next);
    }
}
