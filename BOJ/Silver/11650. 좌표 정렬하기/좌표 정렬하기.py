n = int(input())
ps = [tuple(map(int, input().split()))for _ in range(n)]
for a, b in sorted(ps, key = lambda x: (x[0], x[1])):
  print(a, b)