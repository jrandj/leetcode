package leetcode;

import leetcode.AddTwoNumbers.ListNode;

/**
 * Merge two sorted linked lists and return it as a new list. The new list
 * should be made by splicing together the nodes of the first two lists.
 * 
 * Example:
 * 
 * Input: 1->2->4, 1->3->4 Output: 1->1->2->3->4->4
 */
class MergeTwoSortedLists {
	/**
	 * Merge two sorted linked lists and return the results in a new list.
	 *
	 * @param l1 the head of the first sorted list
	 * @param l2 the head of the second sorted list
	 * @return head the head of the merged list
	 */

	public static ListNode mergeTwoLists(ListNode l1, ListNode l2) {
		ListNode head = new ListNode(0);
		ListNode p = head;
		ListNode p1 = l1;
		ListNode p2 = l2;

		while (p1 != null && p2 != null) {
			// add the smallest ones first
			if (p1.val < p2.val) {
				p.next = p1;
				p1 = p1.next;
			} else {
				p.next = p2;
				p2 = p2.next;
			}
			p = p.next;

		}

		if (p1 != null) {
			p.next = p1;
		}

		if (p2 != null) {
			p.next = p2;
		}
		return head.next;
	}
}
