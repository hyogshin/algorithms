a, b = map(int, input().split())

cs = list(map(int, input().split()))

r = 0
rs = []
for i in range(a):
  for j in range(i+1, a):
    for k in range(j+1, a):
      r = cs[i] + cs[j] + cs[k]
      if r <= b:
        rs.append(r)


print(max(rs))