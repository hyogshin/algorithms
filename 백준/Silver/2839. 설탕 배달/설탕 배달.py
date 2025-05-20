N = int(input())
m = N//3
for i in range(m+1):
  if (N - (3*i))%5 == 0:
    rs = i+ ((N - (3*i))//5)
    print(rs)
    break
else:
  print(-1)
