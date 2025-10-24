class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m, n = len(matrix), len(matrix[0])
        zero = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero.append([i, j])
        
        for x, y in zero:
            for i in range(n):
                matrix[x][i] = 0
            for j in range(m):
                matrix[j][y] = 0
        
        


        