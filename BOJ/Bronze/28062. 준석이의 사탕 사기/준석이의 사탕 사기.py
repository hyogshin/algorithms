n = int(input())
candies = list(map(int, input().split()))

min_odd = max(candies)
cnt = 0
for candy in candies:
  if candy % 2 != 0:
    min_odd = min(min_odd, candy)
    cnt += 1

if cnt % 2 == 0:
  print(sum(candies))
else:
  print(sum(candies) - min_odd)