x, y = map(int, input().split())

origin = (y * 100) // x
z = origin

left = 1
right = 1000000000
ans = 0
while left <= right:
  mid = (left + right) // 2
  z = ((y + mid) * 100) // (x + mid)

  if z > origin:
    ans = mid
    right = mid - 1
  else:
    left = mid + 1

if ans:
  print(ans)
else:
  print(-1)