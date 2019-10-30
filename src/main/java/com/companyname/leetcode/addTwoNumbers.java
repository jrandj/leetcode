package com.companyname.leetcode;


/**
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
*/ 
public class addTwoNumbers {
  
  static class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
   }
  
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
    
}

