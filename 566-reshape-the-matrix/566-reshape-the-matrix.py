class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        if len(mat)*len(mat[0]) != r*c :
            return mat
        else:
            from itertools import chain
            nums = list(chain(*mat))

            out = []
            idx=0
            for i in range(r):
                out.append(nums[idx:idx+c])
                idx +=c
            return out
        