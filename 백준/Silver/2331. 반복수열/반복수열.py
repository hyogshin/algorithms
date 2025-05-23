import sys
input = sys.stdin.readline

a, p = map(int, input().split())
ns = [a]
rs = 0

while 1:
  total = sum(int(d)**p for d in str(a))
  if total in ns:
    rs = ns.index(total)
    break
  ns.append(total)
  a = total

print(rs)