import math 
t = int(input())
for _ in range(t):
  h, w, n = map(int, input().split())
  if n % h == 0:
    if math.ceil(n / h) > 9:
      print(f'{h}{math.ceil(n / h)}')
    else:
      print(f'{h}0{math.ceil(n / h)}')
  else:
    if math.ceil(n / h) > 9:
      print(f'{n % h}{math.ceil(n / h)}')
    else:
      print(f'{n % h}0{math.ceil(n / h)}')