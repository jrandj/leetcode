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
	 */

	public ListNode insertionSortList(ListNode head) {

		// output list
		ListNode sortedList = new ListNode(0);

		// output list dummy for iteration
		ListNode sortedListDummy = new ListNode(0);

		// iterate through input
		while (head != null && head.next != null) {
			// add to output list
			sortedListDummy = sortedList;
			while (sortedListDummy != null) {
				// some base case needed if sortedList is empty
				// if e.g. 4 wanting to add 2, 2 needs to swap with 4
				if (head.val > sortedListDummy.val) {
					sortedListDummy.next = head;
				}

			}
			head = head.next;
		}
		return sortedList.next;
	}
}
