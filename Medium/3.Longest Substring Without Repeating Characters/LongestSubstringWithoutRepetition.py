class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Dictionary to store the last index of each character
        char_map = {}
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            current_char = s[right]
            # If the character is seen and its last index is within the current window, update left
            if current_char in char_map and char_map[current_char] >= left:
                left = char_map[current_char] + 1
            # Update the last occurrence of the character
            char_map[current_char] = right
            # Update the maximum length
            max_length = max(max_length, right - left + 1)
        
        return max_length