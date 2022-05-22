package leetcode;

import org.junit.Assert;

import junit.framework.TestCase;

public class MergeKSortedListsTest extends TestCase {

    /**
     * The first test for MergeKSortedLists.
     */
    public void testMergeKSortedLists1() {
        ListNode tn1 = new ListNode(1);
        ListNode tn2 = new ListNode(1);
        ListNode tn3 = new ListNode(2);
        ListNode tn4 = new ListNode(3);
        ListNode tn5 = new ListNode(4);
        ListNode tn6 = new ListNode(4);
        ListNode tn7 = new ListNode(5);
        ListNode tn8 = new ListNode(6);
        tn1.setNext(tn2);
        tn2.setNext(tn3);
        tn3.setNext(tn4);
        tn4.setNext(tn5);
        tn5.setNext(tn6);
        tn6.setNext(tn7);
        tn7.setNext(tn8);

        ListNode l1n1 = new ListNode(1);
        ListNode l1n2 = new ListNode(4);
        ListNode l1n3 = new ListNode(5);
        l1n1.setNext(l1n2);
        l1n2.setNext(l1n3);

        ListNode l2n1 = new ListNode(1);
        ListNode l2n2 = new ListNode(3);
        ListNode l2n3 = new ListNode(4);
        l2n1.setNext(l2n2);
        l2n2.setNext(l2n3);

        ListNode l3n1 = new ListNode(2);
        ListNode l3n2 = new ListNode(6);
        l3n1.setNext(l3n2);

        ListNode[] input = {l1n1, l2n1, l3n1};
        MergeKSortedLists mergeKSortedLists = new MergeKSortedLists();
        ListNode actualResult = mergeKSortedLists.mergeKLists(input);

        Assert.assertTrue(HelperMethods.compareLists(actualResult, tn1));
    }

    /**
     * The second test for MergeKSortedLists.
     */
    public void testMergeKSortedLists2() {
        ListNode tn1 = null;
        ListNode[] input = null;
        MergeKSortedLists mergeKSortedLists = new MergeKSortedLists();
        ListNode actualResult = mergeKSortedLists.mergeKLists(input);

        Assert.assertTrue(HelperMethods.compareLists(actualResult, tn1));
    }

    /**
     * The third test for MergeKSortedLists.
     */
    public void testMergeKSortedLists3() {
        ListNode tn1 = null;
        ListNode[] input = {tn1};
        MergeKSortedLists mergeKSortedLists = new MergeKSortedLists();
        ListNode actualResult = mergeKSortedLists.mergeKLists(input);

        Assert.assertTrue(HelperMethods.compareLists(actualResult, tn1));
    }

    /**
     * The fourth test for MergeKSortedLists.
     */
    public void testMergeKSortedLists4() {
        ListNode tn1 = new ListNode(1);
        ListNode[] input = {tn1, null};
        MergeKSortedLists mergeKSortedLists = new MergeKSortedLists();
        ListNode actualResult = mergeKSortedLists.mergeKLists(input);

        Assert.assertTrue(HelperMethods.compareLists(actualResult, tn1));
    }

}
