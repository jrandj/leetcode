package leetcode;

final class HelperMethods {

    private HelperMethods() {
        // prevent instantiation
    }

    /**
     * Helper method to compare lists.
     *
     * @param headA The head of the first list
     * @param headB The head of the second list
     * @return true if the lists are equal and false otherwise
     */
    static boolean compareLists(final ListNode headA, final ListNode headB) {
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
