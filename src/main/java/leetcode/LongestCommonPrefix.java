package leetcode;

/**
 * Write a function to find the longest common prefix string amongst an array of
 * strings.
 * 
 * If there is no common prefix, return an empty string "".
 * 
 */
class LongestCommonPrefix {
	/**
	 * Return longest common prefix from an array of Strings
	 *
	 * @param strs the array of Strings
	 * @return the longest common prefix from the array of Strings
	 */

	public static String longestCommonPrefix(String[] strs) {

		if (strs == null || strs.length == 0) {
			return "";
		}

		// find shortest string (longest substring will be the shortest string)
		int shortestString = 0;
		int shortestStringIndex = 0;
		for (int i = 0; i < strs.length; i++) {
			if (strs[i].length() < shortestString) {
				shortestString = strs[i].length();
				shortestStringIndex = i;
			}
		}

		int shortestStringCharacterIndex = 0; // start from the beginning of the shortest string
		String longestCommon = "";
		char currentChar;

		for (int i = 0; i < strs[shortestStringIndex].length(); i++) { // for each character in the shortest string
			currentChar = strs[shortestStringIndex].charAt(shortestStringCharacterIndex);
			for (int j = 0; j < strs.length; j++) { // is this character in every other string?
				if (strs[j].equals("")) {
					return "";
				}

				if (shortestStringCharacterIndex > strs[j].length() - 1) {
					return longestCommon;
				}

				if (strs[j].charAt(shortestStringCharacterIndex) != currentChar) {
					// If all the other strings don't this character, we have found the longest
					return longestCommon.toString();
				}
			}
			shortestStringCharacterIndex++;
			longestCommon += currentChar;
		}
		return longestCommon.toString();
	}
}