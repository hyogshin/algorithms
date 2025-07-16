import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
prefix_sum = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
  for j in range(1, n+1):
    prefix_sum[i][j] = graph[j-1][i-1] + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]

rs = 0
for _ in range(m):
  x1, y1, x2, y2 = map(int, input().rstrip().split())
  rs = prefix_sum[y2][x2] - prefix_sum[y1-1][x2] - prefix_sum[y2][x1-1] + prefix_sum[y1-1][x1-1]
  print(rs)