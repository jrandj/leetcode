package leetcode;

import leetcode.AddTwoNumbers.ListNode;

/**
 * Algorithm of Insertion Sort:
 * 
 * Insertion sort iterates, consuming one input element each repetition, and
 * growing a sorted output list. At each iteration, insertion sort removes one
 * element from the input data, finds the location it belongs within the sorted
 * list, and inserts it there. It repeats until no input elements remain.
 */
class InsertionSortList {
	/**
	 * Sort a linked list using insertion sort.
	 *
	 * @param head the head of the unsorted linked list
	 * @return head the head of sorted linked list
	 * 
	 *         Time: O(n^2), Space: O(1)
	 */
	public ListNode insertionSortList(ListNode head) {
		ListNode dummy = new ListNode(0);
		ListNode p = dummy;
		ListNode cur = head; // makes loop easier to understand (instead of looping head)
		ListNode next = head;

		// iterate over the input list
		while (cur != null) {
			next = cur.next;
			p = dummy;
			// iterate over the (growing) output list
			while (p.next != null && p.next.val <= cur.val) {
				p = p.next;
			}
			// p.next.val is now > cur.val so insert it after cur
			cur.next = p.next;

			// cur is now the head
			p.next = cur;

			// iterate over the input list
			cur = next;
		}

		return dummy.next;
	}
}
