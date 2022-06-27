class Solution:
    def minPartitions(self, n: str) -> int:
        
        lst = list(n)
        
        print(lst)
        
        maxi = 0
        for i in range(len(lst)):
            num = int(lst[i])

            if  num > maxi:
                maxi = num
                
            if maxi == 9:
                break
        
        return maxi