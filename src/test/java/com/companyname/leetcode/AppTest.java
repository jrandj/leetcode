package com.companyname.leetcode;

import java.util.Arrays;

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
