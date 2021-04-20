package leetcode;

import org.junit.Assert;
import junit.framework.TestCase;

public class SortListTest extends TestCase {

    /**
     * The first test for SortList.
     */
    public void testSortList1() {
        ListNode l1n1 = new ListNode(4);
        ListNode l1n2 = new ListNode(2);
        ListNode l1n3 = new ListNode(1);
        ListNode l1n4 = new ListNode(3);
        l1n1.setNext(l1n2);
        l1n2.setNext(l1n3);
        l1n3.setNext(l1n4);

        ListNode l2n1 = new ListNode(1);
        ListNode l2n2 = new ListNode(2);
        ListNode l2n3 = new ListNode(3);
        ListNode l2n4 = new ListNode(4);
        l2n1.setNext(l2n2);
        l2n2.setNext(l2n3);
        l2n3.setNext(l2n4);

        SortList instance = new SortList();
        ListNode actualResult = instance.sortList(l1n1);
        Assert.assertTrue(compareLists(actualResult, l2n1));
    }

    /**
     * The second test for SortList.
     */
    public void testSortList2() {
        ListNode l1n1 = new ListNode(-1);
        ListNode l1n2 = new ListNode(5);
        ListNode l1n3 = new ListNode(3);
        ListNode l1n4 = new ListNode(4);
        ListNode l1n5 = new ListNode(0);
        l1n1.setNext(l1n2);
        l1n2.setNext(l1n3);
        l1n3.setNext(l1n4);
        l1n4.setNext(l1n5);

        ListNode l2n1 = new ListNode(-1);
        ListNode l2n2 = new ListNode(0);
        ListNode l2n3 = new ListNode(3);
        ListNode l2n4 = new ListNode(4);
        ListNode l2n5 = new ListNode(5);
        l2n1.setNext(l2n2);
        l2n2.setNext(l2n3);
        l2n3.setNext(l2n4);
        l2n4.setNext(l2n5);

        SortList instance = new SortList();
        ListNode actualResult = instance.sortList(l1n1);
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

        if (headA.getVal() != headB.getVal()) {
            return false;
        }

        return compareLists(headA.getNext(), headB.getNext());
    }

}
