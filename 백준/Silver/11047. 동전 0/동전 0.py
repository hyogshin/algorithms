n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.reverse()

cnt = 0
for c in coins:
  if c <= k:
    cnt += k//c
    k -= c*(k//c)
  else:
    continue

print(cnt)