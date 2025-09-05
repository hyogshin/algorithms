t = int(input())
for _ in range(t):
  n = int(input())
  a = n % 100
  if (n + 1) % a == 0:
    print('Good')
  else:
    print('Bye')