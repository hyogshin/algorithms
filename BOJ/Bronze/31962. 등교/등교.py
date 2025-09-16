n, x = map(int, input().split())
m = -1
for _ in range(n):
  s, t = map(int, input().split())
  if s + t <= x:
    m = max(s, m)
  
if m == -1:
  print(-1)
else:
  print(m)