class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        x_list = []
        x_list [:0] = str(x)         #convert x str->list
        
        y_list = x_list[::-1]        #reverse x
        
        pali = True
        for idx in range( ceil(len(x_list)/2) ):
            
            if x_list[idx] is not y_list[idx]:
                pali = False
                break
        return pali        
                
        