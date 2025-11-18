class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # this is so easy i can just do dfs and store number of aread of eash island.
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        area = []
        def dfs(x, y):
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n:
                    if grid[nx][ny] == 1 and not visited[nx][ny]:
                        visited[nx][ny] = True
                        self.cnt += 1
                        dfs(nx, ny)
            
            return self.cnt
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    self.cnt = 1
                    visited[i][j] = True
                    area.append(dfs(i, j))
                
        return max(area) if area else 0