n, h = map(int, input().split())
a = list(map(int, input().split()))

cnt = 0
for i in range(n):
  if a[i] <= h:
    cnt += 1

print(cnt)