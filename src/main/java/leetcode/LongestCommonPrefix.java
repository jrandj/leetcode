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

		String longestCommon = "";
		int index = 0;

		for (int i = 0; i < strs.length; i++) {
			char currentChar = strs[i].charAt(index);

			for (int j = 0; j < strs.length; j++) {
				if (strs[j].charAt(index) != currentChar) {
					// If all the other strings don't also have currentChar, we found the longest
					return longestCommon.toString();
				}
			}
			// phew, made it! Let's add another character next time
			index++;
			longestCommon += currentChar;
		}

		return longestCommon.toString();
	}
}
