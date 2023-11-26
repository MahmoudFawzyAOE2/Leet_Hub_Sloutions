class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        
        # Transpose matrix
        for i in range(n): # row
            for j in range(i): #column
                matrix[i][j], matrix[j][i]  = matrix[j][i], matrix[i][j]
        print(matrix)
        
        #reverse every row
        for i in range(n): # row
            for j in range(n//2): #column
                matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j] 
        print(matrix)
        
