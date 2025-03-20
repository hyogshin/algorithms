cnt = int(input())
lns = [0] * cnt

score = 0
total = 0

for i in range(cnt):
  lns[i] = input()

for i in lns:
  total = 0
  score = 0
  for j in i:
    if j == 'O':
      score += 1
      total += score
    else:
      score = 0
  print(total)