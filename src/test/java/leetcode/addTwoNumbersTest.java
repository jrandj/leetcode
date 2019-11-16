package leetcode;

import java.util.ArrayList;
import java.util.List;
import leetcode.AddTwoNumbers.ListNode;
import junit.framework.TestCase;

public class addTwoNumbersTest extends TestCase {
  public void testaddTwoNumbers1() {
    ListNode l1n1 = new ListNode(2);
    ListNode l1n2 = new ListNode(4);
    ListNode l1n3 = new ListNode(3);
    l1n1.next = l1n2;
    l1n2.next = l1n3;

    ListNode l2n1 = new ListNode(5);
    ListNode l2n2 = new ListNode(6);
    ListNode l2n3 = new ListNode(4);
    l2n1.next = l2n2;
    l2n2.next = l2n3;

    List<Integer> testResult = new ArrayList<Integer>();
    List<Integer> actualResult = new ArrayList<Integer>();
    testResult.add(7);
    testResult.add(0);
    testResult.add(8);

    ListNode result = leetcode.AddTwoNumbers.addTwoNumbersSolution(l1n1, l2n1);
    while (result != null) {
      actualResult.add(result.val);
      result = result.next;
    }
    assertEquals(testResult, actualResult);
  }

  public void testaddTwoNumbers2() {
    ListNode l1n1 = new ListNode(5);
    ListNode l2n1 = new ListNode(5);

    List<Integer> testResult = new ArrayList<Integer>();
    List<Integer> actualResult = new ArrayList<Integer>();
    testResult.add(0);
    testResult.add(1);

    ListNode result = leetcode.AddTwoNumbers.addTwoNumbersSolution(l1n1, l2n1);
    while (result != null) {
      actualResult.add(result.val);
      result = result.next;
    }
    assertEquals(testResult, actualResult);
  }
}
