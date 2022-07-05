class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        from itertools import chain
        nums = list(chain(*matrix))
        if target in nums:
            return True
        else: return False