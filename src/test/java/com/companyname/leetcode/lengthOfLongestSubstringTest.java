package com.companyname.leetcode;

import junit.framework.TestCase;

public class lengthOfLongestSubstringTest extends TestCase {
  public void testlengthOfLongestSubstring1() {
    String testString = "abcabcbb";
    int testResult = 3;
    int testOutput = com.companyname.leetcode.lengthOfLongestSubstring.lengthOfLongestSubstringSolution(testString);
    assertEquals(testOutput, testResult);    
  }
  
  public void testlengthOfLongestSubstring2() {
    String testString = "bbbbb";
    int testResult = 1;
    int testOutput = com.companyname.leetcode.lengthOfLongestSubstring.lengthOfLongestSubstringSolution(testString);
    assertEquals(testOutput, testResult);    
  }
  
  public void testlengthOfLongestSubstring3() {
    String testString = "pwwkew";
    int testResult = 3;
    int testOutput = com.companyname.leetcode.lengthOfLongestSubstring.lengthOfLongestSubstringSolution(testString);
    assertEquals(testOutput, testResult);    
  }
 
  public void testlengthOfLongestSubstring4() {
    String testString = "aab";
    int testResult = 2;
    int testOutput = com.companyname.leetcode.lengthOfLongestSubstring.lengthOfLongestSubstringSolution(testString);
    assertEquals(testOutput, testResult);    
  }

  public void testlengthOfLongestSubstring5() {
    String testString = "dvdf";
    int testResult = 3;
    int testOutput = com.companyname.leetcode.lengthOfLongestSubstring.lengthOfLongestSubstringSolution(testString);
    assertEquals(testOutput, testResult);    
  }
  
  public void testlengthOfLongestSubstring6() {
    String testString = " ";
    int testResult = 1;
    int testOutput = com.companyname.leetcode.lengthOfLongestSubstring.lengthOfLongestSubstringSolution(testString);
    assertEquals(testOutput, testResult);    
  }
  
  public void testlengthOfLongestSubstring7() {
    String testString = "";
    int testResult = 0;
    int testOutput = com.companyname.leetcode.lengthOfLongestSubstring.lengthOfLongestSubstringSolution(testString);
    assertEquals(testOutput, testResult);    
  }
  
  public void testlengthOfLongestSubstring8() {
    String testString = "aa";
    int testResult = 1;
    int testOutput = com.companyname.leetcode.lengthOfLongestSubstring.lengthOfLongestSubstringSolution(testString);
    assertEquals(testOutput, testResult);    
  }
  
  public void testlengthOfLongestSubstring9() {
    String testString = "au";
    int testResult = 2;
    int testOutput = com.companyname.leetcode.lengthOfLongestSubstring.lengthOfLongestSubstringSolution(testString);
    assertEquals(testOutput, testResult);    
  }
}
