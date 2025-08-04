import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
heights = list(map(int, input().rstrip().split()))

left = 0
right = max(heights)
ans = 0
while left <= right:
  mid = (left + right) // 2
  meters = 0

  for i in range(n):
    if heights[i] > mid:
      meters += heights[i] - mid
  
  if meters >= m:
    ans = mid
    left = mid + 1
  else:
    right = mid - 1
    
print(ans)
