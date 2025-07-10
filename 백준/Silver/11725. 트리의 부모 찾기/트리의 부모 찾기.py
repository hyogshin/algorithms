import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

n = int(input())
graph = [[] for _ in range(n+1)]
parent = [0] * (n+1)

for _ in range(n-1):
  a, b = map(int, input().rstrip().split())
  graph[a].append(b)
  graph[b].append(a)

def dfs(node):
  for neighbor in graph[node]:
    if parent[neighbor] == 0:
      parent[neighbor] = node
      dfs(neighbor)

parent[1] = -1
dfs(1)

for i in range(2, n+1):
  print(parent[i])