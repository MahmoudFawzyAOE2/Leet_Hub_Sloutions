class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        # check for irregular formats 
        irregular =  {'I':['V','X'], 'V':[], 'X':['L','C'], 'L':[], 'C':['D','M'], 'D':[], 'M':[]}
        Roman_reversed = list(s[::-1])
        # Initialization 
        Num = 0     
        letter_prev = ''
        for letter in Roman_reversed :
            if (letter in irregular.keys()) & (letter_prev in irregular[letter]) : 
                Num = Num - roman_values[letter]
            else:
                Num = Num + roman_values[letter]    
            letter_prev = letter
        return Num