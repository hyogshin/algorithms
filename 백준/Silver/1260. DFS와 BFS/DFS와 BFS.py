import sys
sys.setrecursionlimit(10**4)
from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
marked = [False] * (n+1)

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(n+1):
  graph[i].sort()

rs = []
def dfs(i):
  if not marked[i]:
    rs.append(i)
    marked[i] = True
    for next in graph[i]:
      if not marked[next]:
        dfs(next)

rs_b = []
marked_b = [False] * (n+1)
def bfs(i):
  q = deque()
  q.append(i)
  if not marked_b[i]:
    marked_b[i] = True
  while q:
      a = q.popleft()
      rs_b.append(a)
      for next in graph[a]:
        if not marked_b[next]:
          marked_b[next] = True
          q.append(next)

dfs(v)
bfs(v)

print(' '.join(map(str, rs)))
print(' '.join(map(str, rs_b)))