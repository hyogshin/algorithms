class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # dp = saved minimum height
        # return last cell's dp (row-1, col-1)
        row = len(heights)
        col = len(heights[0])
        INF = 10**7
        dp = [[INF] * col for _ in range(row)]
        # dp[0][0] = 0
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # binary search k
        left, self.right = 0, 0
        for r in heights:
            self.right = max(self.right, max(r))
            
        ans = self.right
        def dfs(x, y, k):
            if x == row - 1 and y == col - 1:
                return True
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < row and 0 <= ny < col:
                    if abs(heights[nx][ny] - heights[x][y]) <= k and not self.visited[nx][ny]:
                        self.visited[nx][ny] = True
                        if dfs(nx, ny, k):
                            return True
            return False       

        while left <= self.right: 
            self.mid = (left + self.right) // 2
            self.visited = [[False] * col for _ in range(row)]
            self.visited[0][0] = True
            dfs(0, 0, self.mid)
            if self.visited[row-1][col-1]:
                ans = self.mid
                self.right = self.mid - 1
                
            else:
                left = self.mid + 1

        # for i in range(col):
        #     for j in range(row):
        #         if not visited[i][j]:
        #             visited[i][j] = True
        #             dfs(i, j)
        
        return ans

        