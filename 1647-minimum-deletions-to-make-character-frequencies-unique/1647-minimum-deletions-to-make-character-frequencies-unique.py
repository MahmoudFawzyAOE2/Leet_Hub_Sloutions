class Solution:
    def minDeletions(self, s: str) -> int:

        frequencies={}
        for letter in s:
            frequencies.setdefault(letter, 0)
            frequencies[letter] +=1
            
                
        print(frequencies)
        
        frequencies_unique = []
        
        mini = 0 
        
        for letter,freq in frequencies.items():
            while freq in frequencies_unique and freq>0:
                mini +=1    
                freq -=1
            frequencies_unique.append(freq)

        return mini