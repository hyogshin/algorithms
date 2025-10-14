t = int(input())

for _ in range(t):
  n = int(input())
  fodder = list(map(int, input().split()))
  days = 1


  if sum(fodder) > n:
      print(1)
      continue
      
  while True:
    tmr = [0] * 6

    for i in range(len(fodder)):
      tmr[i] = (fodder[i] + fodder[(i - 1) % 6] + fodder[(i + 1) % 6] + fodder[(i + 3) % 6])

    if sum(tmr) > n:
      print(days + 1)
      break
    else:
      fodder = tmr
      days += 1