class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        x = nums[1:]
        indices = []
    
        for N1 in nums:
            
            for N2 in x:
            
                if N1 + N2 == target:
                    indices = [nums.index(N1), nums.index( N2 ,nums.index(N1) + 1)]
                    break
                    
            if indices != []:
                break
                
            x.pop(0)
        
        return indices