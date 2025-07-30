from collections import deque

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
marked = [[[0] * 2 for _ in range(m)] for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, broken):
  q = deque()
  q.append((x, y, broken))
  marked[x][y][broken] = 1

  while q:
    x, y, broken = q.popleft()

    if x == n-1 and y == m-1:
      return marked[x][y][broken]

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < m:
        if graph[nx][ny] == '0' and marked[nx][ny][broken] == 0:
          marked[nx][ny][broken] = marked[x][y][broken] + 1
          q.append((nx, ny, broken))
        elif graph[nx][ny] == '1' and broken == 0 and marked[nx][ny][1] == 0:
          marked[nx][ny][1] = marked[x][y][broken] + 1
          q.append((nx, ny, 1))

  return -1 

print(bfs(0, 0, 0))