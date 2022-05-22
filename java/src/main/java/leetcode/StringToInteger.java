package leetcode;

/**
 * Implement atoi which converts a string to an integer. The function first
 * discards as many whitespace characters as necessary until the first
 * non-whitespace character is found. Then, starting from this character, takes
 * an optional initial plus or minus sign followed by as many numerical digits
 * as possible, and interprets them as a numerical value. The string can contain
 * additional characters after those that form the integral number, which are
 * ignored and have no effect on the behaviour of this function. If the first
 * sequence of non-whitespace characters in str is not a valid integral number,
 * or if no such sequence exists because either str is empty or it contains only
 * whitespace characters, no conversion is performed. If no valid conversion
 * could be performed, a zero value is returned. Note: Only the space character
 * ' ' is considered as whitespace character. Assume we are dealing with an
 * environment which could only store integers within the 32-bit signed integer
 * range: [−231, 231 − 1]. If the numerical value is out of the range of
 * representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
 *
 */
final class StringToInteger {

    private StringToInteger() {
        // prevent instantiation
    }

    /**
     * Helper method to convert a string to an integer.
     *
     * @param negative  true if negative and false if otherwise
     * @param intString the String containing integers
     * @return the integer
     */
    public static int resultStringToInteger(final Boolean negative,
            final String intString) {
        int result;

        if (negative == null) {
            return 0;
        }
        try {
            result = Integer.decode(intString);
        } catch (NumberFormatException e) {
            if (intString == null || intString.isEmpty()) {
                return 0;
            }
            // Need to know if the string is negative regardless of whether
            // decode works
            result = negative ? Integer.MIN_VALUE : Integer.MAX_VALUE;
        }

        result = negative ? -1 * result : result;
        return result;
    }

    /**
     * Convert a string to an integer.
     *
     * @param str the input String
     * @return the integer
     */
    public static int myAtoi(final String str) {
        StringBuilder intString = new StringBuilder();
        boolean start = false;
        boolean firstNonZero = false;
        boolean firstNegative = false;
        boolean preceedingZero = false;
        int symbolCount = 0;
        String currentCharString = "";

        if (str.isEmpty() || str == null) {
            return 0;
        }

        for (int i = 0; i < str.length(); i++) {
            Character currentChar = str.charAt(i);
            currentCharString = currentChar.toString();

            if (currentCharString.matches("[1-9]")) {
                firstNonZero = true;
            }
            if (currentCharString.matches("[0]")) {
                preceedingZero = true;
            }
            if (currentCharString.matches("[+-]")) {
                symbolCount++;
            }
            if (currentChar != ' ') {
                start = true;
            }

            // Stop if invalid character after start or symbol after a zero has
            // occurred
            if (!currentCharString.matches("[0-9+-]") && start
                    || currentCharString.matches("[+-]") && preceedingZero) {
                return resultStringToInteger(firstNegative,
                        intString.toString());
                // Only count negative if it is the first occurrence
            } else if (currentCharString.matches("[0-9-]")
                    && symbolCount <= 1) {
                if (currentCharString.matches("-") && !firstNegative
                        && symbolCount == 1 && !firstNonZero) {
                    firstNegative = true;
                    // Build the number string unless it is just leading zeros
                } else if (currentCharString.matches("[1-9]")
                        || currentCharString.equals("0") && firstNonZero) {
                    intString.append(currentCharString);
                }
            }
        }
        return resultStringToInteger(firstNegative, intString.toString());
    }
}
