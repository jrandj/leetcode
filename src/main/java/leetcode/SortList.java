package leetcode;

import leetcode.AddTwoNumbers.ListNode;

/**
 * Sort a linked list in O(n log n) time using constant space complexity.
 */
class SortList {
	/**
	 * Sort a linked list.
	 *
	 * @param head the head of the unsorted linked list
	 * @return head the head of sorted linked list
	 */
	public ListNode sortList(ListNode head) {

		// empty list or list of length 1 is already sorted
		if (head == null || head.next == null) {
			return head;
		}

		ListNode temp = head;
		ListNode fast = temp;
		ListNode slow = temp;

		/*
		 * Split list into halves. Head is start of lhs, temp is end of lhs. Slow is
		 * start of rhs, fast is end of rhs.
		 */
		while (fast != null && fast.next != null) {
			temp = slow;
			slow = slow.next;
			fast = fast.next.next;
		}

		// temp is end of lhs so set next to null (end of rhs already null)
		temp.next = null;

		ListNode lhs = sortList(head);
		ListNode rhs = sortList(slow);
		return mergeLists(lhs, rhs);
	}

	/**
	 * Build sorted list by merging first and second lists.
	 *
	 * @param l1 the head of the first list
	 * @param l2 the head of the second list
	 * @return temp.next the head of the sorted list
	 */
	private ListNode mergeLists(ListNode l1, ListNode l2) {
		// dummy node to allow temp.next (currentNode used for traversal)
		ListNode temp = new ListNode(0);
		ListNode currentNode = temp;

		// build the sorted list with currentNode, increment l1 and l2 if using a value
		while (l1 != null && l2 != null) {
			if (l1.val < l2.val) {
				currentNode.next = l1;
				l1 = l1.next;
			} else {
				currentNode.next = l2;
				l2 = l2.next;
			}
			currentNode = currentNode.next;
		}

		// l2 == null was reached first so l1 value remains
		if (l1 != null) {
			currentNode.next = l1;
			l1 = l1.next;
		}

		// l1 == null was reached first so l2 value remains
		if (l2 != null) {
			currentNode.next = l2;
			l2 = l2.next;
		}

		return temp.next;
	}
}
