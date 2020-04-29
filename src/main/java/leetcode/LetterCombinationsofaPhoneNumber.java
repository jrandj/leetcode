package leetcode;

import java.util.HashSet;
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
class LetterCombinationsofaPhoneNumber {
	/**
	 * Return all possible letter combinations that the digits could represent.
	 *
	 * @param digits the String of digits
	 * @return the List<String> of all possible letter combinations
	 */
	public static List<String> letterCombinations(String digits) {
		List<String> values = new LinkedList<String>(); // this will contain all available letters
		HashSet<String> uniqueCombinations = new HashSet<String>(); // this will contain all unique combinations

		for (int i = 0; i < digits.length(); i++) {
			char ch = digits.charAt(i);

			switch (ch) {
			case '2':
				values.add("abc");
				break;
			case '3':
				values.add("def");
				break;
			case '4':
				values.add("ghi");
				break;
			case '5':
				values.add("jkl");
				break;
			case '6':
				values.add("mno");
				break;
			case '7':
				values.add("pqrs");
				break;
			case '8':
				values.add("tuv");
				break;
			case '9':
				values.add("wxyz");
				break;
			}
		}

		System.out.println("values: " + values);
		String combination = "";

		for (int i = 0; i < values.size(); i++) {
			for (int j = i + 1; j < values.size(); j++) {
				for (int k = 0; k < values.get(i).length(); k++) {
					for (int l = 0; l < values.get(j).length(); l++) {
						// brute force all of the combinations
						combination = new StringBuilder().append(values.get(i).charAt(k))
								.append(values.get(j).charAt(l)).toString();
						System.out.println("combination: " + combination);
						// let the HashSet sort out uniqueness
						uniqueCombinations.add(String.valueOf(combination));
					}
				}
			}
		}

		LinkedList<String> returnList = new LinkedList<>(uniqueCombinations);
		System.out.println("returnList: " + returnList);
		return returnList;
	}
}
