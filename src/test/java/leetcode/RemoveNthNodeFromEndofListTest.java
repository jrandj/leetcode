package leetcode;

import junit.framework.Assert;
import junit.framework.TestCase;

public class RemoveNthNodeFromEndofListTest extends TestCase {
	public void testGenerateParenthesesTest1() {
		ListNode l1n1 = new ListNode(1);
		ListNode l1n2 = new ListNode(2);
		ListNode l1n3 = new ListNode(3);
		ListNode l1n4 = new ListNode(4);
		ListNode l1n5 = new ListNode(5);
		l1n1.next = l1n2;
		l1n2.next = l1n3;
		l1n3.next = l1n4;
		l1n4.next = l1n5;

		ListNode l2n1 = new ListNode(1);
		ListNode l2n2 = new ListNode(2);
		ListNode l2n3 = new ListNode(3);
		ListNode l2n5 = new ListNode(5);
		l2n1.next = l2n2;
		l2n2.next = l2n3;
		l2n3.next = l2n5;

		int n = 2;
		ListNode actualResult = leetcode.RemoveNthNodeFromEndofList.removeNthFromEnd(l1n1, n);
		Assert.assertTrue(CompareLists(actualResult, l2n1));
	}

	public void testGenerateParenthesesTest2() {
		ListNode l1n1 = new ListNode(1);
		ListNode l1n2 = new ListNode(2);
		l1n1.next = l1n2;

		ListNode l2n1 = new ListNode(2);

		int n = 2;
		ListNode actualResult = leetcode.RemoveNthNodeFromEndofList.removeNthFromEnd(l1n1, n);
		Assert.assertTrue(CompareLists(actualResult, l2n1));
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