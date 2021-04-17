package leetcode;

import junit.framework.Assert;
import junit.framework.TestCase;

public class MergeTwoSortedListsTest extends TestCase {
    /**
     * The first test for MergeTwoSortedLists.
     */
    public void testMergeTwoSortedLists1() {
        ListNode l1n1 = new ListNode(1);
        ListNode l1n2 = new ListNode(2);
        ListNode l1n3 = new ListNode(4);
        l1n1.setNext(l1n2);
        l1n2.setNext(l1n3);

        ListNode l2n1 = new ListNode(1);
        ListNode l2n2 = new ListNode(3);
        ListNode l2n3 = new ListNode(4);
        l2n1.setNext(l2n2);
        l2n2.setNext(l2n3);

        ListNode l3n1 = new ListNode(1);
        ListNode l3n2 = new ListNode(1);
        ListNode l3n3 = new ListNode(2);
        ListNode l3n4 = new ListNode(3);
        ListNode l3n5 = new ListNode(4);
        ListNode l3n6 = new ListNode(4);
        l3n1.setNext(l3n2);
        l3n2.setNext(l3n3);
        l3n3.setNext(l3n4);
        l3n4.setNext(l3n5);
        l3n5.setNext(l3n6);

        ListNode actualResult = leetcode.MergeTwoSortedLists.mergeTwoLists(l1n1,
                l2n1);
        Assert.assertTrue(compareLists(actualResult, l3n1));
    }

    /**
     * Helper method to compare 2 lists.
     *
     * @param headA The head node of the first linked list
     * @param headB The head node of the second linked list
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
