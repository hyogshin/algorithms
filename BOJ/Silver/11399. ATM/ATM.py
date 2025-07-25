n = int(input())
t = list(map(int, input().split()))
t.sort(reverse=True)
total = 0
for i, j in enumerate(t):
  total += (i+1)*j
print(total)