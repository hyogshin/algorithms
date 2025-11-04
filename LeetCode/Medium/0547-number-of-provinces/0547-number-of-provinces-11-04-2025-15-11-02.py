class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.n = len(isConnected)
        self.provinces = 0
        self.visited = [[False] * self.n for _ in range(self.n)]
        self.isConnected = isConnected

        for i in range(self.n):
            for j in range(self.n):
                if isConnected[i][j] == 1 and not self.visited[i][j]:
                    self.visited[i][j] = True
                    self.visited[j][i] = True
                    self.dfs(i, j)
                    self.provinces += 1
        return self.provinces

    def dfs(self, x, y):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < self.n and 0 <= ny < self.n:
                if self.isConnected[nx][ny] == 1 and not self.visited[nx][ny]:
                    self.visited[nx][ny] = True
                    self.visited[ny][nx] = True
                    self.dfs(nx, ny)

    