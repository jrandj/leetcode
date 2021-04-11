package leetcode;

import java.util.LinkedList;
import java.util.List;

/**
 * Given a string containing digits from 2-9 inclusive, return all possible
 * letter combinations that the number could represent.
 *
 * A mapping of digit to letters (just like on the telephone buttons) is given
 * below. Note that 1 does not map to any letters.
 *
 * Example:
 *
 * Input: "23" Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
 * Note:
 *
 * Although the above answer is in lexicographical order, your answer could be
 * in any order you want.
 */
final class LetterCombinationsofaPhoneNumber {

    private LetterCombinationsofaPhoneNumber() {
        // prevent instantiation
    }

    /**
     * Return all possible letter combinations that the digits could represent.
     *
     * @param digits the String of digits
     * @return the List<String> of all possible letter combinations
     */
    public static List<String> letterCombinations(final String digits) {

        LinkedList<String> returnList = new LinkedList<String>();

        if (digits.isEmpty()) {
            return returnList;
        }

        String[] mapping = new String[] {"0", "1", "abc", "def", "ghi", "jkl",
                "mno", "pqrs", "tuv", "wxyz"};
        returnList.add("");
        for (int i = 0; i < digits.length(); i++) {
            int index = Character.getNumericValue(digits.charAt(i));
            while (returnList.peek().length() == i) {
                String top = returnList.remove();
                for (char ch : mapping[index].toCharArray()) {
                    returnList.add(top + ch);
                }
            }
        }

        return returnList;
    }
}
