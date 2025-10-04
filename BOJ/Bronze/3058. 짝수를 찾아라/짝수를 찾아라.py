t = int(input())


for _ in range(t):
  s = 0
  m = 0
  even = []
  
  nums = list(map(int, input().split()))
  for n in nums:
    if n % 2 == 0:
      even.append(n)

  s = sum(even)
  m = min(even)
  print(s, m)