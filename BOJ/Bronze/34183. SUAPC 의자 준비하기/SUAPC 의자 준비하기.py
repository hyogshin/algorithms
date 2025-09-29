n, m, a, b = map(int, input().split())
if ((n * 3) - m) > 0:
  print(((n * 3) - m) * a + b)
else:
  print(0)