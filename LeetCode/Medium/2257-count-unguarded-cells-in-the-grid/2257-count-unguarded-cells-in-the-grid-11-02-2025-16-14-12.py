class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [['c'] * n for _ in range(m)]
        guarded = [[False] * n for _ in range(m)]

        for i, j in guards:
            grid[i][j] = 'g'
        for i, j in walls:
            grid[i][j] = 'w'

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i, j in guards:
            for dx, dy in directions:
                x = i + dx
                y = j + dy
                while 0 <= x < m and 0 <= y < n and grid[x][y] not in ('g', 'w'):
                    guarded[x][y] = True
                    x += dx
                    y += dy
            
        
        for i, j in guards:
            guarded[i][j] = True
        for i, j in walls:
            guarded[i][j] = True
        
        cnt = 0
        for i in range(m):
            for j in range(n):
                if guarded[i][j] == False:
                    cnt += 1
        
        return cnt
        