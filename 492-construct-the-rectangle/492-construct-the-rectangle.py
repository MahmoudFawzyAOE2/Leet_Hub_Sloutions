from math import sqrt

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        
        w = floor(sqrt(area))
        
        for i in range(w):
            L = area / w 
            
            if L % 1 == 0:
                break   
            else:
                w-=1
                
        return [int(L),w]   