class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(x, y):
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < m and 0 <= ny < n:
                    if grid[nx][ny] == '1' and not visited[nx][ny]:
                        visited[nx][ny] = True
                        dfs(nx, ny)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    cnt += 1
                    visited[i][j] = True
                    dfs(i, j)

        return cnt


        