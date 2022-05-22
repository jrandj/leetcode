package leetcode;

import org.junit.Assert;
import junit.framework.TestCase;

public class RemoveNthNodeFromEndofListTest extends TestCase {

    /**
     * The first test for GenerateParentheses.
     */
    public void testGenerateParenthesesTest1() {
        ListNode l1n1 = new ListNode(1);
        ListNode l1n2 = new ListNode(2);
        ListNode l1n3 = new ListNode(3);
        ListNode l1n4 = new ListNode(4);
        ListNode l1n5 = new ListNode(5);
        l1n1.setNext(l1n2);
        l1n2.setNext(l1n3);
        l1n3.setNext(l1n4);
        l1n4.setNext(l1n5);

        ListNode l2n1 = new ListNode(1);
        ListNode l2n2 = new ListNode(2);
        ListNode l2n3 = new ListNode(3);
        ListNode l2n5 = new ListNode(5);
        l2n1.setNext(l2n2);
        l2n2.setNext(l2n3);
        l2n3.setNext(l2n5);

        int n = 2;
        ListNode actualResult = leetcode.RemoveNthNodeFromEndofList
                .removeNthFromEnd(l1n1, n);
        Assert.assertTrue(HelperMethods.compareLists(actualResult, l2n1));
    }

    /**
     * The second test for GenerateParentheses.
     */
    public void testGenerateParenthesesTest2() {
        ListNode l1n1 = new ListNode(1);
        ListNode l1n2 = new ListNode(2);
        l1n1.setNext(l1n2);

        ListNode l2n1 = new ListNode(2);

        int n = 2;
        ListNode actualResult = leetcode.RemoveNthNodeFromEndofList
                .removeNthFromEnd(l1n1, n);
        Assert.assertTrue(HelperMethods.compareLists(actualResult, l2n1));
    }

}
