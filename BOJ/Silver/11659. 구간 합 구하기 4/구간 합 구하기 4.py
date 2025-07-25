import sys
input = sys.stdin.readline

n, m  = map(int, input().rstrip().split())
ns = list(map(int, input().rstrip().split()))
ms = [list(map(int, input().rstrip().split())) for _ in range(m)]

rs = [0] * (n+1)
rs[0] = ns[0]
for i in range(1, n):
  rs[i] = rs[i-1] + ns[i]

for i in range(m):
  print(rs[ms[i][1]-1] - rs[ms[i][0]-2])