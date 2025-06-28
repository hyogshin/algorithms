n, x = map(int, input().split())
ns = list(map(int, input().split()))

rs = []
for i in range(n):
  if ns[i] < x:
    rs.append(ns[i])

print(*rs)