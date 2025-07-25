from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

cnt = 0
def bfs(x, y):
  global cnt
  q = deque()
  q.append((x, y))
  visited[x][y]
  
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m:
        if not visited[nx][ny] and graph[nx][ny] != 'X':
          visited[nx][ny] = True
          if graph[nx][ny] == 'P':
            cnt += 1
          q.append((nx, ny))

for i in range(n):
  for j in range(m):
    if graph[i][j] == 'I':
      visited[i][j] = True
      bfs(i, j)
      print(cnt if cnt > 0 else 'TT')
      exit()