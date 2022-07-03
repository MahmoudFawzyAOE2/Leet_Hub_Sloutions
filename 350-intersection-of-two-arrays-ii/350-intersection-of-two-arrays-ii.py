class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        intersection = []
        for i in range(len(nums1)):
            
            if nums1[i] in nums2 :
                intersection.append(nums1[i])
                nums2.remove(nums1[i])
                
        return intersection 