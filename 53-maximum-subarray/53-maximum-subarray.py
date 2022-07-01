class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        cur = maxi = nums[0]
        for n in range(1,len(nums)):
            
            cur = max([nums[n], nums[n]+cur])
            maxi = max([maxi,cur])
        
        return maxi
                