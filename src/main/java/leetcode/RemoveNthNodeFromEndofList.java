package leetcode;

/**
 * Given a linked list, remove the n-th node from the end of list and return its
 * head.
 * 
 * Example:
 * 
 * Given linked list: 1->2->3->4->5, and n = 2.
 * 
 * After removing the second node from the end, the linked list becomes
 * 1->2->3->5. Note:
 * 
 * Given n will always be valid.
 * 
 * Follow up:
 * 
 * Could you do this in one pass?
 */
class RemoveNthNodeFromEndofList {
	/**
	 * Remove the n-th node from the end of the list and return the head.
	 *
	 * @param head the linked list head node
	 * @param n    the n'th node
	 * @return head the linked list head node
	 */
	public static ListNode removeNthFromEnd(ListNode head, int n) {
		// find the index of the nth element
		// if index, cut node out of list

		int len = 0;
		ListNode dummyHead = head;
		while (dummyHead.next != null) {
			dummyHead = dummyHead.next;
			len++;
		}

		int index = len - n;
		len = 0;
		
		dummyHead = head;
		while (index != len) {
			dummyHead = dummyHead.next;
			len++;
		}
		
		head = dummyHead.next.next;

		return head;
	}
}

class ListNode {
	int val;
	ListNode next;

	ListNode() {
	}

	ListNode(int val) {
		this.val = val;
	}

	ListNode(int val, ListNode next) {
		this.val = val;
		this.next = next;
	}
}
