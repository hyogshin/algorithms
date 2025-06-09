import math
n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())
cnt = 0
for i in size:
  if i == 0:
    continue
  else:
    cnt += math.ceil(i/t)

print(cnt)
print(n//p, n-((n//p)*p))