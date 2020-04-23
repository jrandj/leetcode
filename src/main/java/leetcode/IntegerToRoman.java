package leetcode;

/**
 * Roman numerals are represented by seven different symbols: I, V, X, L, C, D
 * and M.
 * 
 * Symbol Value I 1 V 5 X 10 L 50 C 100 D 500 M 1000
 * 
 * For example, two is written as II in Roman numeral, just two one's added
 * together. Twelve is written as, XII, which is simply X + II. The number
 * twenty seven is written as XXVII, which is XX + V + II.
 * 
 * Roman numerals are usually written largest to smallest from left to right.
 * However, the numeral for four is not IIII. Instead, the number four is
 * written as IV. Because the one is before the five we subtract it making four.
 * The same principle applies to the number nine, which is written as IX. There
 * are six instances where subtraction is used:
 * 
 * I can be placed before V (5) and X (10) to make 4 and 9. X can be placed
 * before L (50) and C (100) to make 40 and 90. C can be placed before D (500)
 * and M (1000) to make 400 and 900. Given an integer, convert it to a roman
 * numeral. Input is guaranteed to be within the range from 1 to 3999.
 *
 */
class IntegerToRoman {
	/**
	 * Return int representation of Roman numeral
	 *
	 * @param num the int representation of the Roman numeral
	 * @return the String representation of the Roman numeral
	 */
	public static String intToRoman(int num) {
		int[] n = { 1000, 900, 500, 490, 450, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 };
		String[] symbols = { "M", "CM", "D", "CDXC", "CDL", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" };
		String returnString = "";

		for (int i = 0; i < n.length; i++) {
			while (num / n[i] != 0) {
				returnString += symbols[i];
				num -= n[i];
			}

		}
		return returnString;
	}
}