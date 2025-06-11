import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = [[] for _ in range(n+1)]
marked = [False] * (n+1)

for _ in range(m):
  a, b = map(int, input().rstrip().split())
  graph[a].append(b)
  graph[b].append(a)

def dfs(i):
  for next in graph[i]:
    if not marked[next]:
      marked[next] = True
      dfs(next)

cnt = 0
for i in range(1, n+1):
  if not marked[i]:
    marked[i] = True
    cnt += 1
    dfs(i)

print(cnt)