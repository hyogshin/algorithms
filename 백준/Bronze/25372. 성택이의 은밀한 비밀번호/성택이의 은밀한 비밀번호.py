n = int(input())
ps = [input() for _ in range(n)]

for i in range(n):
  if 6<=len(ps[i])<=9:
    print('yes')
  else:
    print('no')