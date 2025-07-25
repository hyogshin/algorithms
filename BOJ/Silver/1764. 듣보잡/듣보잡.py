n, m = map(int, input().split())

h = set()
s = set()
for _ in range(n):
  h.add(input())

for _ in range(m):
  s.add(input())

rs = sorted(s & h)
print(len(rs))
for r in rs:
  print(r)