package leetcode;

import org.junit.Assert;

import junit.framework.TestCase;

public class SwapNodesInPairsTest extends TestCase {

    /**
     * The first test for SwapNodesInPairsTest.
     */
    public void testSwapNodesInPairsTest1() {
        ListNode l1n1 = new ListNode(1);
        ListNode l1n2 = new ListNode(2);
        ListNode l1n3 = new ListNode(3);
        ListNode l1n4 = new ListNode(4);
        l1n1.setNext(l1n2);
        l1n2.setNext(l1n3);
        l1n3.setNext(l1n4);

        ListNode l2n1 = new ListNode(2);
        ListNode l2n2 = new ListNode(1);
        ListNode l2n3 = new ListNode(4);
        ListNode l2n4 = new ListNode(3);
        l2n1.setNext(l2n2);
        l2n2.setNext(l2n3);
        l2n3.setNext(l2n4);

        SwapNodesInPairs swapNodesInPairs = new SwapNodesInPairs();
        ListNode actualResult = swapNodesInPairs.swapPairs(l1n1);
        Assert.assertTrue(HelperMethods.compareLists(actualResult, l2n1));
    }

    /**
     * The second test for SwapNodesInPairsTest.
     */
    public void testSwapNodesInPairsTest2() {
        SwapNodesInPairs swapNodesInPairs = new SwapNodesInPairs();
        ListNode actualResult = swapNodesInPairs.swapPairs(null);
        Assert.assertTrue(HelperMethods.compareLists(actualResult, null));
    }

    /**
     * The third test for SwapNodesInPairsTest.
     */
    public void testSwapNodesInPairsTest3() {
        ListNode l1n1 = new ListNode(1);
        ListNode l2n1 = new ListNode(1);

        SwapNodesInPairs swapNodesInPairs = new SwapNodesInPairs();
        ListNode actualResult = swapNodesInPairs.swapPairs(l1n1);
        Assert.assertTrue(HelperMethods.compareLists(actualResult, l2n1));
    }

}
