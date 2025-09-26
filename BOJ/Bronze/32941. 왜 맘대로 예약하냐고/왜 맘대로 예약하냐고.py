t, x = map(int, input().split())
n = int(input())
attendable = True
for _ in range(n):
  k = int(input())
  a = list(map(int, input().split()))
  if x not in a:
    attendable = False


if attendable:
  print('YES')
else:
  print('NO')