from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
marked = [[False] * m for _ in range(n)]

dx = [1, 0 , -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
  q = deque()
  q.append((x, y))
  marked[x][y] = True

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < m:
        if not marked[nx][ny] and graph[nx][ny] == 1:
          marked[nx][ny] = True
          q.append((nx, ny))
          graph[nx][ny] = graph[x][y] + 1

found = False
for i in range(n):
  for j in range(m):
    if graph[i][j] == 2:
      graph[i][j] = 0
      bfs(i, j)
      found = True
      break
  if found:
    break

for i in range(n):
  for j in range(m):
    if graph[i][j] == 1 and not marked[i][j]:
      graph[i][j] = -1

for row in graph:
  print(*row)