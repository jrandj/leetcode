package leetcode;

import junit.framework.Assert;
import junit.framework.TestCase;
import leetcode.AddTwoNumbers.ListNode;

public class MergeTwoSortedListsTest extends TestCase {
	public void testMergeTwoSortedLists1() {
		ListNode l1n1 = new ListNode(1);
		ListNode l1n2 = new ListNode(2);
		ListNode l1n3 = new ListNode(4);
		l1n1.next = l1n2;
		l1n2.next = l1n3;

		ListNode l2n1 = new ListNode(1);
		ListNode l2n2 = new ListNode(3);
		ListNode l2n3 = new ListNode(4);
		l2n1.next = l2n2;
		l2n2.next = l2n3;
		
		ListNode l3n1 = new ListNode(1);
		ListNode l3n2 = new ListNode(1);
		ListNode l3n3 = new ListNode(2);
		ListNode l3n4 = new ListNode(3);
		ListNode l3n5 = new ListNode(4);
		ListNode l3n6 = new ListNode(4);
		l3n1.next = l3n2;
		l3n2.next = l3n3;
		l3n3.next = l3n4;
		l3n4.next = l3n5;
		l3n5.next = l3n6;
		
		ListNode actualResult = leetcode.MergeTwoSortedLists.mergeTwoLists(l1n1, l2n1);
		Assert.assertTrue(CompareLists(actualResult, l3n1));
	}


	boolean CompareLists(ListNode headA, ListNode headB) {
		if ((headA == null) ^ (headB == null))
			return false;

		if ((headA == null) && (headB == null))
			return true;

		if (headA.val != headB.val)
			return false;
		return CompareLists(headA.next, headB.next);
	}

}