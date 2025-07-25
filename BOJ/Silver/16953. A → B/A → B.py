import sys
input = sys.stdin.readline
a, b = map(int, input().rstrip().split())

cnt = 1
while b != a:
  if b < a:
    print('-1')
    break
  if b%2 == 0:
    b = b//2
    cnt += 1
  elif b%10 == 1:
    b = b//10
    cnt += 1
  else:
    print('-1')
    break

if a == b:
  print(cnt)