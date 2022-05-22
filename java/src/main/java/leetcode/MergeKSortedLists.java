package leetcode;

import java.util.PriorityQueue;

/**
 * You are given an array of k linked-lists lists, each linked-list is sorted in
 * ascending order. Merge all the linked-lists into one sorted linked-list and
 * return it.
 */
final class MergeKSortedLists {

    /**
     * Sort an array of k linked-list lists using a min-heap.
     *
     * The time complexity is O(N log(M*N)) where N is the number of lists and M
     * is the number of nodes in a list. Adding and removing an element in a
     * min-heap is log(N).
     *
     * The space complexity is O(M*N) as that is the size of the min-heap.
     *
     * @param lists the input lists
     * @return the head node of the sorted list
     */
    public ListNode mergeKLists(final ListNode[] lists) {

        if (lists == null || lists.length == 0) {
            return null;
        }

        ListNode dummyHead = new ListNode(-1);
        ListNode head = dummyHead;
        dummyHead.setNext(head);
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();

        for (int i = 0; i < lists.length; i++) {
            while (lists[i] != null) {
                minHeap.add(lists[i].getVal());
                lists[i] = lists[i].getNext();
            }
        }

        if (minHeap.isEmpty()) {
            return null;
        }

        while (!minHeap.isEmpty()) {
            head.setNext(new ListNode(minHeap.remove()));
            head = head.getNext();

        }

        return dummyHead.getNext();
    }

}
