n = int(input())
k = '666'

cnt = 0
i = 1
while 1:
  if k in str(i):
    cnt += 1
  if cnt == n:
    print(i)
    break
  i += 1