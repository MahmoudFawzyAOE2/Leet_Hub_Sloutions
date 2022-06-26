from math import sqrt

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        
        w = sqrt(area)
        
        w = floor(w)
         
        
        for i in range(w):
            
            L = area / w 
            
            if L % 1 == 0:
                L = int(L)
                break
                
            else:
                w = w -1
                
        return [L,w]
    
    
            
            