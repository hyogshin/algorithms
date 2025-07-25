l = int(input())
ws = list(input())

sum = 0
for i, j in enumerate(ws):
  sum += (ord(j)-96)*(31**i)

print(sum)
