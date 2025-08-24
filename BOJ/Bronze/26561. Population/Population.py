n = int(input())

for _ in range(n):
  p, t = map(int, input().split())
  estimated = p + (t//4) - (t//7)
  print(estimated)