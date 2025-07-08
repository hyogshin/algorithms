equation = input().split('-')

s = 0
total = []
for e in equation:
  tmp = e.split('+')
  for i in tmp:
    s += int(i)
  total.append(s)
  s = 0

ans = total[0]
for i in range(1, len(total)):
  ans -= total[i]

print(ans)