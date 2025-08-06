from collections import defaultdict
n = int(input())
ns = map(int, input().split())
m = int(input())
ms = map(int, input().split())

rs = defaultdict(int)
for n in ns:
  rs[n] += 1

for m in ms:
  rs[m] += 1
  if rs[m] == 2:
    print(1, end=' ')
  else:
    print(0, end=' ')