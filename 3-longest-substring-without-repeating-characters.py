class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        current_substring = ''
        longest_substring = ''

        for letter in s:
            if  letter not in current_substring :
                current_substring += letter
            else : 
                index = current_substring.find(letter)
                current_substring = current_substring[index+1:] + letter
                
            if len(current_substring) > len(longest_substring) :
                longest_substring = current_substring
        
        return len(longest_substring)
