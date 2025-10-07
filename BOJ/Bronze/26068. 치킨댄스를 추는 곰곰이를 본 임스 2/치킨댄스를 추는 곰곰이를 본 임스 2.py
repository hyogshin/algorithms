n = int(input())
cnt = 0
for _ in range(n):
  coupon = input().split('-')
  if int(coupon[-1]) <= 90:
    cnt += 1

print(cnt)