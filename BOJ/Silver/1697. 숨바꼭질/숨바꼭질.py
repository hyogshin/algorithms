from collections import deque

n, m = map(int, input().split())
visited = [False] * 100001
position = [0] * 100001

def bfs(x, target):
  q = deque()
  q.append((x))
  visited[x] = True

  while q:
    x = q.popleft()
    for i in [x-1, x+1, 2*x]:
      if 0 <= i < 100001:
        if not visited[i]:
          visited[i] = True
          position[i]  = position[x] + 1
          q.append(i)
          if i == target:
            break

if n == m:
  print(0)
else:
  bfs(n, m)
  print(position[m])