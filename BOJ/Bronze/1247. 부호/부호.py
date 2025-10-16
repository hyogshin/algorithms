for _ in range(3):
  n = int(input())
  s = [int(input()) for _ in range(n)]

  if sum(s) == 0:
    print('0')
  elif sum(s) < 0:
    print('-')
  else:
    print('+')