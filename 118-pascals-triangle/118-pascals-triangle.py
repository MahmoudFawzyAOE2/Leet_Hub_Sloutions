class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        pascal = []
        for n in range(numRows):
            row = [1]
            if n==1 : row.append(1)
                
            if n>=2 :
                for i in range(n-1):
                    row.append(pascal[n-1][i]+pascal[n-1][i+1])
                row.append(1)
                
            pascal.append(row)
        return pascal