package leetcode;

/**
 * Roman numerals are represented by seven different symbols: I, V, X, L, C, D
 * and M.
 *
 * Symbol Value I 1 V 5 X 10 L 50 C 100 D 500 M 1000 For example, two is written
 * as II in Roman numeral, just two one's added together. Twelve is written as,
 * XII, which is simply X + II. The number twenty seven is written as XXVII,
 * which is XX + V + II.
 *
 * Roman numerals are usually written largest to smallest from left to right.
 * However, the numeral for four is not IIII. Instead, the number four is
 * written as IV. Because the one is before the five we subtract it making four.
 * The same principle applies to the number nine, which is written as IX. There
 * are six instances where subtraction is used:
 *
 * I can be placed before V (5) and X (10) to make 4 and 9. X can be placed
 * before L (50) and C (100) to make 40 and 90. C can be placed before D (500)
 * and M (1000) to make 400 and 900. Given a roman numeral, convert it to an
 * integer. Input is guaranteed to be within the range from 1 to 3999.
 *
 */
final class RomanToInteger {

    private RomanToInteger() {
        // prevent instantiation
    }

    /**
     * Return int representation of a Roman numeral.
     *
     * @param s String representation of the Roman numeral
     * @return int representation of the Roman numeral
     */
    public static int romanToInt(final String s) {
        int total = 0;

        if (s.length() == 1) {
            return getCharValue(s.charAt(0));
        }

        for (int i = 0; i < s.length() - 1; i++) {
            char currentChar = s.charAt(i);
            char nextChar = s.charAt(i + 1);

            if (currentChar == nextChar
                    || getCharValue(currentChar) > getCharValue(nextChar)) {
                total += getCharValue(currentChar);
            } else if (getCharValue(currentChar) < getCharValue(nextChar)) {
                total -= getCharValue(currentChar);
            }
        }

        total += getCharValue(s.charAt(s.length() - 1));
        return total;

    }

    /**
     * Return int value for a Roman numeral character.
     *
     * @param ch Roman numerical char
     * @return value Roman numerical char int value
     */
    private static int getCharValue(final char ch) {
        int value = 0;
        switch (ch) {
        case 'I':
            value = 1;
            break;
        case 'V':
            value = 5;
            break;
        case 'X':
            value = 10;
            break;
        case 'L':
            value = 50;
            break;
        case 'C':
            value = 100;
            break;
        case 'D':
            value = 500;
            break;
        case 'M':
            value = 1000;
            break;
        default:
        }
        return value;
    }
}
