import sys
sys.setrecursionlimit(10**4)

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
marked = [[False] * n for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
cnt = 0
def dfs(x, y):
  global cnt
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < n and 0 <= ny < n:
      if not marked[nx][ny] and graph[nx][ny] == 1:
        cnt += 1
        marked[nx][ny] = True
        dfs(nx, ny)

rs = []
for i in range(n):
  for j in range(n):
    if not marked[i][j] and graph[i][j] == 1:
      marked[i][j] = True
      cnt = 1
      dfs(i, j)
      rs.append(cnt)

rs.sort()
print(len(rs))
print('\n'.join(map(str, rs)))