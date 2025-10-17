n = int(input())
m = int(input())
ans = m
for i in range(n):
  entrance, ex = map(int, input().split())
  m -= ex
  m += entrance

  ans = max(ans, m)

  if m < 0:
    ans = 0
    break

print(ans)