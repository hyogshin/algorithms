n, m = map(int, input().split())
graph = [list(input()) for _ in range(m)]
marked = [[False] * n for _ in range(m)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, target):
  cnt = 1
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < m and 0 <= ny < n:
      if not marked[nx][ny] and graph[nx][ny] == target:
        marked[nx][ny] = True
        cnt += dfs(nx, ny, target)
  return cnt

w = 0
b = 0
for i in range(m):
  for j in range(n):
    if not marked[i][j] and graph[i][j] == 'W':
      marked[i][j] = True
      w += dfs(i, j, 'W') ** 2
      cnt = 1
    elif not marked[i][j] and graph[i][j] == 'B':
      marked[i][j] = True
      b += dfs(i, j, 'B') ** 2
      cnt = 1

print(w, b)