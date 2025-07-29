from collections import defaultdict
n = int(input())
ns = list(map(int, input().split()))
m = int(input())
ms = list(map(int, input().split()))

h = defaultdict(int)
for i in ns:
  h[i] += 1

rs = []
for i in ms:
  rs.append(h[i])

print(*rs)
