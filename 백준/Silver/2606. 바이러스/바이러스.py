n = int(input())
e = int(input())

# 그래프 만들기
graph = [[] for _ in range(n+1)]
marked = [False] * (n+1)

for _ in range(e):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)


cnt = 0
def dfs(n):
  global cnt
  if not marked[n]:
    marked[n] = True
    for next in graph[n]:
      if not marked[next]:
        cnt += 1
        dfs(next)
  return cnt

print(dfs(1))