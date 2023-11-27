class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        while True:
            try :
                if nums[k] == nums[k+1]:
                    nums.pop(k+1)
                else: k+=1
            except: break    
        return len(nums)
