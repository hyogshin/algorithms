x, y = map(int, input().split())

repunit = 0
for i in range(x):
  repunit += 10**i

for i in range(y):
  repunit += 10**i

print(repunit)