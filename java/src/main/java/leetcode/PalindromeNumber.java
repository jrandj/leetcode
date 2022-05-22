package leetcode;

/**
 * Determine whether an integer is a palindrome. An integer is a palindrome when
 * it reads the same backward as forward.
 */
public final class PalindromeNumber {

    private PalindromeNumber() {
        // prevent instantiation
    }

    /**
     * Determine whether an integer is a palindrome.
     *
     * @param px the input parameter
     * @return true if the input number is a palindrome and false otherwise
     */
    public static boolean isPalindrome2(final int px) {
        int x = px;

        // if x is 0 by definition it is a palindrome
        if (x == 0) {
            return true;
        }

        // if x is negative or 1, 10, 100 etc. it is not a palindrome
        if (x < 0 || x % 10 == 0) {
            return false;
        }

        int reversedInt = 0;
        while (x > reversedInt) {
            // get the last digit of x
            int pop = x % 10;
            // look at the previous digit
            x = x / 10;
            reversedInt = (reversedInt * 10) + pop;
        }

        return x == reversedInt || x == reversedInt / 10;

    }

    /**
     * Determine whether an integer is a palindrome using a naive approach.
     *
     * @param x the input parameter
     * @return true if the input number is a palindrome and false otherwise
     */
    public static boolean isPalindromeNaive(final int x) {
        String intString = Integer.toString(x);
        StringBuilder reverseString = new StringBuilder();

        for (int i = intString.length() - 1; i >= 0; i--) {
            if (intString.charAt(i) == '+' || intString.charAt(i) == '-') {
                break;
            }
            reverseString.append(intString.charAt(i));
        }

        return intString.equals(reverseString.toString());
    }
}
