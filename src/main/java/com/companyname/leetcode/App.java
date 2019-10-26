package com.companyname.leetcode;

import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;


public class App {

    /**
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    */
    public static int[] twoSum(int[] nums, int target){
    for (int i=0; i<(nums.length); i++){
        	for (int j=0; j<(nums.length); j++){
        		if(nums[i]+nums[j] == target) {
        			if(i!=j) {
        				return new int[] {i, j};
        			}
        		}
        	}
        }
        return null;
	}
    
    
    /**
    You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.
    */ 
    public static ListNode addTwoNumbers(ListNode l1, ListNode l2) {
      ListNode dummyHead = new ListNode(0);
      ListNode l3 = dummyHead;
      int l1Val, l2Val, sum;
      int carry = 0, digit = 0;
      
      while(l1 != null || l2 != null) {
        
        if(l1 != null) {
          l1Val = l1.val;
        } else {
          l1Val = 0;
        }
        
        if(l2 != null) {
          l2Val = l2.val;
        } else {
          l2Val = 0;
        }
       
        sum = l1Val + l2Val + carry; 
        carry = sum/10;
        digit = sum%10;
        ListNode newNode = new ListNode(digit);
        l3.next = newNode;
      
        if(l1 != null) {
          l1 = l1.next;
        }
        if(l2 != null) {
          l2 = l2.next;
        }
        l3 = l3.next;
      }
      
      if(carry > 0) {
        ListNode newNode = new ListNode(carry);
        l3.next = newNode;
        l3 = l3.next;
      }
           
      return dummyHead.next;
    }
    
    
	public static void main(String[] args){
	  ListNode l1n1 = new ListNode(2);
	  ListNode l1n2 = new ListNode(4);
	  ListNode l1n3 = new ListNode(3);
	  l1n1.next = l1n2;
	  l1n2.next = l1n3;
	  l1n3.next = null;
	  ListNode l2n1 = new ListNode(5);
	  ListNode l2n2 = new ListNode(6);
	  ListNode l2n3 = new ListNode(4);
	  l2n1.next = l2n2;
	  l2n2.next = l2n3;
	  l2n3.next = null;
	  
	  ListNode result = addTwoNumbers(l1n1, l2n1);

    }
}
