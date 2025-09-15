a, p, c = map(int, input().split())
m = max(a + c, p)

if m == p:
  print(p)
else:
  print(a + c)