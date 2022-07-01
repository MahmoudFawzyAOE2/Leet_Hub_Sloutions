class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        frequencies={}
        for num in nums:
            frequencies.setdefault(num, 0)
            frequencies[num] +=1
        
        print(frequencies)
        dub = False
        for f in frequencies.values():
            if f > 1 :
                dub = True
        
        return dub