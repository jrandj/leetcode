package com.companyname.leetcode;

import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;


/**
 * Unit test for simple App.
 */
public class AppTest extends TestCase
{
	
  
	public void testtwoSumExpectedResult1() {
		int[] result;
		int[] nums = {2, 7, 11, 15};
		int target = 9;
		int[] testResult = {0, 1};

		result = com.companyname.leetcode.App.twoSum(nums, target);
		assertEquals(Arrays.toString(testResult), Arrays.toString(result));
	}
	
	
	public void testtwoSumExpectedResult2() {
		int[] result;
		int[] nums = {3, 2, 3};
		int target = 6;
		int[] testResult = {0, 2};

		result = com.companyname.leetcode.App.twoSum(nums, target);
		assertEquals(Arrays.toString(testResult), Arrays.toString(result));
	}
	
	
	public void testtwoSumExpectedResult3() {
		int[] result;
		int[] nums = {2,5,5,11};
		int target = 10;
		int[] testResult = {1, 2};

		result = com.companyname.leetcode.App.twoSum(nums, target);
		assertEquals(Arrays.toString(testResult), Arrays.toString(result));
	}
	
	
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
       
      ListNode result = com.companyname.leetcode.App.addTwoNumbers(l1n1, l2n1);
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

      ListNode result = com.companyname.leetcode.App.addTwoNumbers(l1n1, l2n1);
      while (result != null) {
        actualResult.add(result.val);
        result = result.next;
      }
      assertEquals(testResult, actualResult);
    }
	   
    /**
     * Create the test case
     *
     * @param testName name of the test case
     */
    public AppTest( String testtwoSumExpectedResult1 )
    {
        super( testtwoSumExpectedResult1 );
    }


    /**
     * @return the suite of tests being tested
     */
    public static Test suite()
    {
        return new TestSuite( AppTest.class );
    }

    
    /**
     * Rigourous Test :-)
     */
    public void testApp()
    {
        assertTrue( true );
    }
}
